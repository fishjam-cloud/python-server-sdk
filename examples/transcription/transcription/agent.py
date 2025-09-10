import asyncio

from fishjam.agent import Agent
from transcription.worker import BackgroundWorker

from .transcription import TranscriptionSession


class TranscriptionAgent:
    def __init__(self, room_id: str, agent: Agent, worker: BackgroundWorker):
        self._room_id = room_id
        self._agent = agent
        self._sessions: dict[str, TranscriptionSession] = {}
        self._worker = worker
        self._task: asyncio.Task[None] | None = None

    async def _start(self):
        async with self._agent.connect() as session:
            print(f"Agent connected to room {self._room_id}")

            async for track_data in session.receive():
                if track_data.peer_id not in self._sessions:
                    return
                self._sessions[track_data.peer_id].transcribe(track_data.data)

        print(f"Agent disconnected from room {self._room_id}")

    def _handle_transcription(self, peer_id: str, text: str):
        print(f"Peer {peer_id} in room {self._room_id} said: {text}")

    def on_peer_enter(self, peer_id: str):
        if peer_id in self._sessions:
            return

        if len(self._sessions) == 0:
            self._task = self._worker.run_in_background(self._start())

        session = TranscriptionSession(lambda t: self._handle_transcription(peer_id, t))
        self._sessions[peer_id] = session
        self._worker.run_in_background(session.start(peer_id))

    def on_peer_leave(self, peer_id: str):
        if peer_id not in self._sessions:
            return

        self._sessions.pop(peer_id).end()

        if len(self._sessions) == 0 and self._task is not None:
            self._task.cancel()
            self._task = None
