import asyncio

from fishjam.agent import Agent, AgentResponseTrackData
from transcription.worker import BackgroundWorker

from .transcription import TranscriptionSession


class TranscriptionAgent:
    def __init__(self, room_id: str, agent: Agent, worker: BackgroundWorker):
        self._room_id = room_id
        self._agent = agent
        self._sessions: dict[str, TranscriptionSession] = {}
        self._disconnect = asyncio.Event()
        self._worker = worker

        @agent.on_track_data
        def _(track_data: AgentResponseTrackData):
            if track_data.peer_id not in self._sessions:
                return
            self._sessions[track_data.peer_id].transcribe(track_data.data)

    async def _start(self):
        async with self._agent:
            print(f"Agent connected to room {self._room_id}")
            await self._disconnect.wait()
        self._disconnect.clear()
        print(f"Agent disconnected from room {self._room_id}")

    def _stop(self):
        self._disconnect.set()

    def _handle_transcription(self, peer_id: str, text: str):
        print(f"Peer {peer_id} in room {self._room_id} said: {text}")

    def on_peer_enter(self, peer_id: str):
        if peer_id in self._sessions:
            return

        if len(self._sessions) == 0:
            self._worker.run_in_background(self._start())

        session = TranscriptionSession(lambda t: self._handle_transcription(peer_id, t))
        self._sessions[peer_id] = session
        self._worker.run_in_background(session.start(peer_id))

    def on_peer_leave(self, peer_id: str):
        if peer_id not in self._sessions:
            return

        self._sessions[peer_id].end()
        self._sessions.pop(peer_id)

        if len(self._sessions) == 0:
            self._stop()
