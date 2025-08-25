from fishjam import FishjamClient, Room
from fishjam.errors import NotFoundError
from transcription.worker import BackgroundWorker

from .agent import TranscriptionAgent
from .config import FISHJAM_ID, FISHJAM_TOKEN, FISHJAM_URL

fishjam = FishjamClient(
    FISHJAM_ID,
    FISHJAM_TOKEN,
    fishjam_url=FISHJAM_URL,
)


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
            fishjam.create_agent(self.room.id),
            self._worker,
        )

    def get_agent(self):
        return self.agent
