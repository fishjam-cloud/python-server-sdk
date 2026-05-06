# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring, redefined-outer-name

import pytest

from fishjam import FishjamClient, Room, RoomOptions
from fishjam.errors import HTTPError
from tests.support.env import FISHJAM_ID, FISHJAM_MANAGEMENT_TOKEN


class _TrackingFishjamClient(FishjamClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._tracked_room_ids: list[str] = []

    def create_room(self, options: RoomOptions | None = None) -> Room:
        room = super().create_room(options)
        self._tracked_room_ids.append(room.id)
        return room

    def cleanup_tracked_rooms(self) -> None:
        for room_id in self._tracked_room_ids:
            try:
                self.delete_room(room_id)
            except HTTPError:
                pass
        self._tracked_room_ids.clear()


@pytest.fixture
def room_api():
    client = _TrackingFishjamClient(FISHJAM_ID, FISHJAM_MANAGEMENT_TOKEN)
    yield client
    client.cleanup_tracked_rooms()
