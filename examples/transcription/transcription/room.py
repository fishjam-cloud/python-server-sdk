from fishjam import AgentOptions, FishjamClient, Room
from fishjam.errors import NotFoundError
from fishjam.integrations.gemini import GeminiIntegration
from transcription.worker import BackgroundWorker

from .agent import TranscriptionAgent
from .config import FISHJAM_ID, FISHJAM_TOKEN

fishjam = FishjamClient(FISHJAM_ID, FISHJAM_TOKEN)


class RoomService:
    def __init__(self, worker: BackgroundWorker):
        self._worker = worker
        self._create_room()

    def get_room(self) -> Room:
        try:
            self.room = fishjam.get_room(self.room.id)
        except NotFoundError:
            self._create_room()
        return self.room

    def _create_room(self):
        self.room = fishjam.create_room()
        self._create_agent()

    def _create_agent(self):
        self.agent = TranscriptionAgent(
            self.room.id,
            fishjam.create_agent(
                self.room.id,
                AgentOptions(output=GeminiIntegration.GEMINI_INPUT_AUDIO_SETTINGS),
            ),
            self._worker,
        )

    def get_agent(self):
        return self.agent
