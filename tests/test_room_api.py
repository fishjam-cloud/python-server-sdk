# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods, missing-module-docstring


import os

import pytest

from fishjam import (
    FishjamClient,
    PeerOptions,
    RoomOptions,
)
from fishjam._openapi_client.models import (
    PeerStatus,
    RoomConfig,
    RoomConfigVideoCodec,
)
from fishjam.api._fishjam_client import Peer, Room
from fishjam.errors import (
    BadRequestError,
    NotFoundError,
    ServiceUnavailableError,
    UnauthorizedError,
)

HOST = "fishjam" if os.getenv("DOCKER_TEST") == "TRUE" else "localhost"
FISHJAM_URL = f"http://{HOST}:5002"
MANAGEMENT_TOKEN = "development"

MAX_PEERS = 10
CODEC_H264 = "h264"


class TestAuthentication:
    def test_invalid_token(self):
        room_api = FishjamClient(fishjam_url=FISHJAM_URL, management_token="invalid")

        with pytest.raises(UnauthorizedError):
            room_api.create_room()

    def test_valid_token(self):
        room_api = FishjamClient(
            fishjam_url=FISHJAM_URL, management_token=MANAGEMENT_TOKEN
        )

        room = room_api.create_room()
        all_rooms = room_api.get_all_rooms()

        assert room in all_rooms


@pytest.fixture
def room_api():
    return FishjamClient(fishjam_url=FISHJAM_URL, management_token=MANAGEMENT_TOKEN)


class TestCreateRoom:
    def test_no_params(self, room_api):
        room = room_api.create_room()

        config = RoomConfig(
            max_peers=None,
            video_codec=None,
            webhook_url=None,
            peerless_purge_timeout=None,
            peer_disconnected_timeout=None,
        )
        config.__setitem__("roomId", room.config.__getitem__("roomId"))

        assert room == Room(
            config=config,
            id=room.id,
            peers=[],
        )

        assert room in room_api.get_all_rooms()

    def test_valid_params(self, room_api):
        options = RoomOptions(max_peers=MAX_PEERS, video_codec=CODEC_H264)
        room = room_api.create_room(options)

        config = RoomConfig(
            max_peers=MAX_PEERS,
            video_codec=RoomConfigVideoCodec(CODEC_H264),
            webhook_url=None,
            peerless_purge_timeout=None,
            peer_disconnected_timeout=None,
        )
        config.__setitem__("roomId", room.config.__getitem__("roomId"))

        assert room == Room(
            config=config,
            id=room.id,
            peers=[],
        )

        assert room in room_api.get_all_rooms()

    def test_invalid_max_peers(self, room_api):
        options = RoomOptions(max_peers="10")

        with pytest.raises(BadRequestError):
            room_api.create_room(options)

    def test_invalid_video_codec(self, room_api):
        with pytest.raises(ValueError):
            options = RoomOptions(video_codec="h420")
            room_api.create_room(options)


class TestDeleteRoom:
    def test_valid(self, room_api):
        room = room_api.create_room()

        room_api.delete_room(room.id)
        assert room not in room_api.get_all_rooms()

    def test_invalid_id(self, room_api):
        with pytest.raises(BadRequestError):
            room_api.delete_room("invalid_id")

    def test_id_not_found(self, room_api):
        with pytest.raises(NotFoundError):
            room_api.delete_room("515c8b52-168b-4b39-a227-4d6b4f102a56")


class TestGetAllRooms:
    def test_valid(self, room_api):
        room = room_api.create_room()
        all_rooms = room_api.get_all_rooms()

        assert isinstance(all_rooms, list)
        assert room in all_rooms


class TestGetRoom:
    def test_valid(self, room_api: FishjamClient):
        room = room_api.create_room()

        config = RoomConfig(
            max_peers=None,
            video_codec=None,
            webhook_url=None,
            peerless_purge_timeout=None,
            peer_disconnected_timeout=None,
        )
        config.__setitem__("roomId", room.config.__getitem__("roomId"))

        assert Room(
            peers=[],
            id=room.id,
            config=config,
        ) == room_api.get_room(room.id)

    def test_invalid(self, room_api: FishjamClient):
        with pytest.raises(BadRequestError):
            room_api.get_room("invalid_id")

    def test_id_not_found(self, room_api):
        with pytest.raises(NotFoundError):
            room_api.get_room("515c8b52-168b-4b39-a227-4d6b4f102a56")


class TestCreatePeer:
    def _assert_peer_created(
        self, room_api, webrtc_peer, room_id, server_metadata=None
    ):
        server_metadata = server_metadata or {}

        peer = Peer(
            id=webrtc_peer.id,
            type="webrtc",
            status=PeerStatus("disconnected"),
            tracks=[],
            metadata={"peer": {}, "server": server_metadata},
        )

        room = room_api.get_room(room_id)
        assert peer in room.peers

    def test_with_specified_options(self, room_api: FishjamClient):
        options = PeerOptions(enable_simulcast=True)

        room = room_api.create_room()
        peer, _token = room_api.create_peer(room.id, options=options)

        self._assert_peer_created(room_api, peer, room.id)

    def test_with_metadata(self, room_api: FishjamClient):
        options = PeerOptions(metadata={"is_test": True})
        room = room_api.create_room()
        peer, _token = room_api.create_peer(room.id, options=options)

        self._assert_peer_created(room_api, peer, room.id, {"is_test": True})

    def test_default_options(self, room_api: FishjamClient):
        room = room_api.create_room()
        peer, _token = room_api.create_peer(room.id)

        self._assert_peer_created(room_api, peer, room.id)

    def test_peer_limit_reached(self, room_api: FishjamClient):
        config = RoomOptions(max_peers=1)
        room = room_api.create_room(config)
        peer, _token = room_api.create_peer(room.id)

        self._assert_peer_created(room_api, peer, room.id)

        with pytest.raises(ServiceUnavailableError):
            room_api.create_peer(room.id)


class TestDeletePeer:
    def test_valid(self, room_api: FishjamClient):
        room = room_api.create_room()
        peer, _token = room_api.create_peer(room.id)
        room_api.delete_peer(room.id, peer.id)

        assert [] == room_api.get_room(room.id).peers

    def test_invalid(self, room_api: FishjamClient):
        room = room_api.create_room()

        with pytest.raises(NotFoundError):
            room_api.delete_peer(room.id, peer_id="invalid_peer_id")


class TestRefreshPeerToken:
    def test_valid(self, room_api: FishjamClient):
        room = room_api.create_room()
        peer, token = room_api.create_peer(room.id)
        refreshed_token = room_api.refresh_peer_token(room.id, peer.id)

        assert token != refreshed_token

    def test_invalid(self, room_api: FishjamClient):
        room = room_api.create_room()

        with pytest.raises(NotFoundError):
            room_api.refresh_peer_token(room.id, peer_id="invalid_peer_id")
