from asyncio import Event, Queue, TaskGroup
from typing import Callable

from google.genai.live import AsyncSession
from google.genai.types import Blob

from fishjam.integrations.gemini import GeminiIntegration

from .config import TRANSCRIPTION_CONFIG, TRANSCRIPTION_MODEL


class TranscriptionSession:
    def __init__(self, on_text: Callable[[str], None]):
        self._gemini = GeminiIntegration.create_client()
        self._audio_queue = Queue[bytes]()
        self._end_event = Event()
        self._model = TRANSCRIPTION_MODEL
        self._on_text = on_text

    async def start(self, peer_id: str):
        async with self._gemini.aio.live.connect(
            model=self._model,
            config=TRANSCRIPTION_CONFIG,
        ) as session:
            async with TaskGroup() as tg:
                send_task = tg.create_task(self._send_loop(session))
                recv_task = tg.create_task(self._recv_loop(session))

                print(f"Started transcription session for peer {peer_id}")

                await self._end_event.wait()

                send_task.cancel()
                recv_task.cancel()
            print(f"Stopped transcription session for peer {peer_id}")

    def transcribe(self, audio: bytes):
        self._audio_queue.put_nowait(audio)

    def end(self):
        self._end_event.set()

    async def _send_loop(self, session: AsyncSession):
        while True:
            audio_frame = await self._audio_queue.get()
            await session.send_realtime_input(
                audio=Blob(data=audio_frame, mime_type="audio/pcm;rate=16000")
            )

    async def _recv_loop(self, session: AsyncSession):
        while True:
            acc = ""
            async for res in session.receive():
                if (
                    (content := res.server_content)
                    and (transcription := content.input_transcription)
                    and (text := transcription.text)
                ):
                    acc += text

            if acc:
                self._on_text(acc)
