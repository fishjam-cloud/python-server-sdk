import asyncio

from poet_chat.agent import poet_runner
from poet_chat.config import (
    AGENT_OPTIONS,
    fishjam_client,
)
from poet_chat.notifier import make_notifier

from fishjam.agent import OutgoingAudioTrackOptions


async def main():
    room = fishjam_client.create_room()
    _, token = fishjam_client.create_peer(room.id)
    print(f"Join the chat with the following token: {token}")

    agent = fishjam_client.create_agent(room.id, AGENT_OPTIONS)
    async with (
        agent.connect() as fishjam_session,
        await poet_runner.run() as openai_session,
    ):
        track = await fishjam_session.add_track(
            OutgoingAudioTrackOptions(
                sample_rate=24000, metadata={"type": "microphone"}
            )
        )

        async def _openai_recv():
            msg = ""
            async for event in openai_session:
                if event.type == "audio":
                    audio = event.audio.data
                    await track.send_chunk(audio)
                elif event.type == "audio_interrupted":
                    await track.interrupt()
                elif event.type == "raw_model_event":
                    if event.data.type == "input_audio_transcription_completed":
                        print(f"Peer said:\n{event.data.transcript}\n")
                    elif event.data.type == "transcript_delta":
                        msg += event.data.delta
                    elif event.data.type == "turn_ended":
                        print(f"Agent said:\n{msg}\n")
                        msg = ""
                    elif event.data.type == "error":
                        print(event.data.error)
                        raise RuntimeError("Unexpected error from OpenAI API!")
                    elif event.data.type == "exception":
                        raise event.data.exception
                    elif event.data.type == "raw_server_event":
                        match event.data.data:
                            case {"response": {"status": "failed"}}:
                                print(event.data.data)
                                raise RuntimeError("Raw server error from OpenAI API!")

        async def _fishjam_recv():
            async for event in fishjam_session.receive():
                await openai_session.send_audio(event.data)

        async with asyncio.TaskGroup() as tg:
            tg.create_task(make_notifier(openai_session).connect())
            tg.create_task(_openai_recv())
            tg.create_task(_fishjam_recv())


if __name__ == "__main__":
    asyncio.run(main())
