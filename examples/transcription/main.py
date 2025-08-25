from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI
from transcription.notifier import make_notifier
from transcription.room import RoomService, fishjam
from transcription.worker import async_worker

from fishjam import PeerOptions, SubscribeOptions

_room_service: RoomService | None = None


def get_room_service():
    if not _room_service:
        raise RuntimeError("Application skipped lifespan events!")
    return _room_service


@asynccontextmanager
async def lifespan(_app: FastAPI):
    async with async_worker() as worker:
        global _room_service
        _room_service = RoomService(worker)
        notifier = make_notifier(_room_service)
        worker.run_in_background(notifier.connect())

        yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def get_peer(room_service: Annotated[RoomService, Depends(get_room_service)]):
    _peer, token = fishjam.create_peer(
        room_service.get_room().id,
        PeerOptions(subscribe=SubscribeOptions()),
    )
    return token
