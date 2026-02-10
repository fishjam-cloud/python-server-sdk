import asyncio

from fishjam.agent import Agent, AgentSession, IncomingTrackData, IncomingTrackImage
from fishjam.integrations.gemini import GeminiIntegration

from .config import IMAGE_CAPTURE_INTERVAL
from .session import MultimodalSession
from .worker import BackgroundWorker


class MultimodalAgent:
    def __init__(self, room_id: str, agent: Agent, worker: BackgroundWorker):
        self._room_id = room_id
        self._agent = agent
        self._worker = worker
        self._task: asyncio.Task[None] | None = None
        self._capture_task: asyncio.Task[None] | None = None

        # Session management per peer
        self._sessions: dict[str, MultimodalSession] = {}

        # Track caching: peer_id -> set of video track_ids
        self._peer_tracks: dict[str, set[str]] = {}
        # Reverse lookup: track_id -> peer_id
        self._track_to_peer: dict[str, str] = {}

        # Agent session reference for capturing images and sending audio
        self._agent_session: AgentSession | None = None

    async def _start(self):
        async with self._agent.connect() as session:
            self._agent_session = session

            # Create output track for Gemini audio responses

            self._output_track = await session.add_track(
                GeminiIntegration.GEMINI_OUTPUT_AUDIO_SETTINGS
            )
            print(f"Agent connected to room {self._room_id}")

            async for message in session.receive():
                match message:
                    case IncomingTrackImage(track_id=track_id, data=data):
                        peer_id = self._track_to_peer.get(track_id)
                        if peer_id and peer_id in self._sessions:
                            self._sessions[peer_id].send_image(data)
                            print(f"Sent image from {track_id} to {peer_id}")

                    case IncomingTrackData(peer_id=peer_id, data=data):
                        if peer_id in self._sessions:
                            self._sessions[peer_id].send_audio(data)

        self._agent_session = None
        print(f"Agent disconnected from room {self._room_id}")

    async def _periodic_capture(self):
        while True:
            await asyncio.sleep(IMAGE_CAPTURE_INTERVAL)

            if not self._agent_session:
                continue

            # Capture images from all known video tracks
            for track_id in self._track_to_peer.keys():
                try:
                    await self._agent_session.capture_image(track_id)
                    print(f"Requested image capture for track {track_id}")
                except Exception as e:
                    print(f"Error capturing image from track {track_id}: {e}")

    def _handle_audio_response(self, peer_id: str, audio: bytes):
        if self._output_track:
            self._worker.run_in_background(self._output_track.send_chunk(audio))

    def on_peer_enter(self, peer_id: str):
        if peer_id in self._sessions:
            return

        # Initialize track cache for this peer
        self._peer_tracks[peer_id] = set()

        # Start agent connection if this is the first peer
        if len(self._sessions) == 0:
            self._task = self._worker.run_in_background(self._start())
            capture_coro = self._periodic_capture()
            self._capture_task = self._worker.run_in_background(capture_coro)

        # Create multimodal session for this peer
        def on_audio(audio: bytes, pid: str = peer_id):
            self._handle_audio_response(pid, audio)

        session = MultimodalSession(on_audio)
        self._sessions[peer_id] = session
        self._worker.run_in_background(session.start(peer_id))

    def on_peer_leave(self, peer_id: str):
        if peer_id not in self._sessions:
            return

        # Clean up track cache
        if peer_id in self._peer_tracks:
            for track_id in self._peer_tracks[peer_id]:
                self._track_to_peer.pop(track_id, None)
            del self._peer_tracks[peer_id]

        # End the session
        self._sessions.pop(peer_id).end()

        # Stop agent if no more sessions
        if len(self._sessions) == 0:
            if self._task is not None:
                self._task.cancel()
                self._task = None
            if self._capture_task is not None:
                self._capture_task.cancel()
                self._capture_task = None

    def on_track_added(self, peer_id: str, track_id: str, is_video: bool):
        if not is_video:
            return

        if peer_id not in self._peer_tracks:
            self._peer_tracks[peer_id] = set()

        self._peer_tracks[peer_id].add(track_id)
        self._track_to_peer[track_id] = peer_id
        print(f"Added video track {track_id} for peer {peer_id}")

    def on_track_removed(self, peer_id: str, track_id: str, is_video: bool):
        if not is_video:
            return

        if peer_id in self._peer_tracks:
            self._peer_tracks[peer_id].discard(track_id)
        self._track_to_peer.pop(track_id, None)
        print(f"Removed video track {track_id} for peer {peer_id}")
