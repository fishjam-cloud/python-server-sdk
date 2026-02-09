import asyncio
from asyncio import Event, Queue, TaskGroup
from typing import Callable

from google.genai.live import AsyncSession
from google.genai.types import Blob

from fishjam.integrations.gemini import GeminiIntegration

from .config import MULTIMODAL_CONFIG, MULTIMODAL_MODEL


class MultimodalSession:
    def __init__(self, on_audio_response: Callable[[bytes], None]):
        self._gemini = GeminiIntegration.create_client()
        self._audio_queue: Queue[bytes] = Queue()
        self._image_queue: Queue[bytes] = Queue()
        self._end_event = Event()
        self._model = MULTIMODAL_MODEL
        self._on_audio = on_audio_response

    async def start(self, peer_id: str):
        async with self._gemini.aio.live.connect(
            model=self._model,
            config=MULTIMODAL_CONFIG,
        ) as session:
            async with TaskGroup() as tg:
                send_task = tg.create_task(self._send_loop(session))
                recv_task = tg.create_task(self._recv_loop(session))

                print(f"Started multimodal session for peer {peer_id}")

                await self._end_event.wait()

                send_task.cancel()
                recv_task.cancel()
            print(f"Stopped multimodal session for peer {peer_id}")

    def send_audio(self, audio: bytes):
        self._audio_queue.put_nowait(audio)

    def send_image(self, image: bytes):
        self._image_queue.put_nowait(image)

    def end(self):
        self._end_event.set()

    async def _send_loop(self, session: AsyncSession):
        while True:
            audio_task = asyncio.create_task(self._audio_queue.get())
            image_task = asyncio.create_task(self._image_queue.get())

            done, pending = await asyncio.wait(
                [audio_task, image_task],
                return_when=asyncio.FIRST_COMPLETED,
            )

            for task in pending:
                task.cancel()

            for task in done:
                if task is audio_task:
                    audio_frame = task.result()
                    await session.send_realtime_input(
                        audio=Blob(
                            data=audio_frame,
                            mime_type=GeminiIntegration.GEMINI_AUDIO_MIME_TYPE,
                        )
                    )
                elif task is image_task:
                    print("sending video")
                    image_data = task.result()
                    await session.send_realtime_input(
                        media=Blob(
                            data=image_data,
                            mime_type="image/jpeg",
                        )
                    )

    async def _recv_loop(self, session: AsyncSession):
        while True:
            async for message in session.receive():
                if (
                    (content := message.server_content)
                    and (model_turn := content.model_turn)
                    and (parts := model_turn.parts)
                ):
                    for part in parts:
                        if part.inline_data and part.inline_data.data:
                            self._on_audio(part.inline_data.data)
                if content and content.model_turn:
                    if content.turn_complete:
                        print("\n--- Turn Finished ---")
