import json
from contextlib import contextmanager
from unittest.mock import patch

import httpx

from fishjam import CompositionClient, FishjamClient
from fishjam.utils import get_livestream_whep_url, get_livestream_whip_url

ROOM_ID = "room-1"
COMPOSITION_ID = "comp-1"
LOCAL_COMPOSITION_URL = "http://localhost:8000"
FISHJAM_ID = "abc123"


@contextmanager
def mock_response(status: int = 201):
    requests: list[httpx.Request] = []

    def handle_request(request: httpx.Request, **_kwargs):
        request.read()
        requests.append(request)
        return httpx.Response(status, json={})

    with patch.object(
        httpx.HTTPTransport, "handle_request", side_effect=handle_request
    ):
        yield requests


class TestForwardRoomTracks:
    def test_points_fishjam_at_the_composition_it_should_feed(self):
        compositions = CompositionClient(
            management_token="token", composition_url=LOCAL_COMPOSITION_URL
        )
        fishjam = FishjamClient(FISHJAM_ID, "token")

        with mock_response() as requests:
            fishjam.forward_room_tracks(
                ROOM_ID, compositions.composition_url(COMPOSITION_ID)
            )

        assert (
            requests[0].url.path
            == "/api/v1/connect/abc123/room/room-1/track_forwardings"
        )
        assert requests[0].method == "POST"
        assert json.loads(requests[0].content) == {
            "compositionURL": f"{LOCAL_COMPOSITION_URL}/api/composition/comp-1",
            "selector": "all",
        }


class TestLivestreamWhipUrl:
    def test_derives_the_address_from_a_bare_fishjam_id(self):
        assert (
            FishjamClient(FISHJAM_ID, "token").livestream_whip_url()
            == "https://fishjam.io/api/v1/live/api/whip"
        )

    def test_keeps_the_host_when_the_fishjam_id_is_a_full_url(self):
        client = FishjamClient(
            "https://cloud.fishjam.work/api/v1/connect/abc123", "token"
        )

        assert (
            client.livestream_whip_url()
            == "https://cloud.fishjam.work/api/v1/live/api/whip"
        )

    def test_derives_the_address_without_a_client(self):
        assert (
            get_livestream_whip_url(FISHJAM_ID)
            == "https://fishjam.io/api/v1/live/api/whip"
        )


class TestLivestreamWhepUrl:
    def test_derives_the_address_from_a_bare_fishjam_id(self):
        assert (
            FishjamClient(FISHJAM_ID, "token").livestream_whep_url()
            == "https://fishjam.io/api/v1/live/api/whep"
        )

    def test_keeps_the_host_when_the_fishjam_id_is_a_full_url(self):
        client = FishjamClient(
            "https://cloud.fishjam.work/api/v1/connect/abc123", "token"
        )

        assert (
            client.livestream_whep_url()
            == "https://cloud.fishjam.work/api/v1/live/api/whep"
        )

    def test_derives_the_address_without_a_client(self):
        assert (
            get_livestream_whep_url(FISHJAM_ID)
            == "https://fishjam.io/api/v1/live/api/whep"
        )


class TestRoomCompositionInfo:
    ROOM = {
        "id": ROOM_ID,
        "config": {"roomType": "conference"},
        "peers": [],
        "compositionInfo": {
            "compositionUrl": "http://localhost:8000/api/composition/comp-1",
            "forwardings": [
                {"inputId": "in-1", "peerId": "peer-1", "videoTrackId": "track-1"}
            ],
        },
    }

    def test_reports_which_composition_the_room_feeds(self):
        def handle_request(request: httpx.Request, **_kwargs):
            request.read()
            return httpx.Response(200, json={"data": self.ROOM})

        with patch.object(
            httpx.HTTPTransport, "handle_request", side_effect=handle_request
        ):
            room = FishjamClient(FISHJAM_ID, "token").get_room(ROOM_ID)

        assert room.composition_info is not None
        assert (
            room.composition_info.composition_url
            == "http://localhost:8000/api/composition/comp-1"
        )
        assert room.composition_info.forwardings[0].peer_id == "peer-1"

    def test_leaves_it_empty_when_the_room_feeds_nothing(self):
        def handle_request(request: httpx.Request, **_kwargs):
            request.read()
            room = {k: v for k, v in self.ROOM.items() if k != "compositionInfo"}
            return httpx.Response(200, json={"data": room})

        with patch.object(
            httpx.HTTPTransport, "handle_request", side_effect=handle_request
        ):
            room = FishjamClient(FISHJAM_ID, "token").get_room(ROOM_ID)

        assert room.composition_info is None
