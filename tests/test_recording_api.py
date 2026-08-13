import json
from unittest.mock import patch

import httpx
import pytest

from fishjam import FishjamClient, Recording
from fishjam.errors import (
    InternalServerError,
    NotFoundError,
    QuotaExceededError,
    ServiceUnavailableError,
    UnauthorizedError,
)
from fishjam.recording import CompositionSource, RecordingStatus
from tests.support.env import FISHJAM_ID, FISHJAM_MANAGEMENT_TOKEN

NONEXISTENT_RECORDING_ID = "515c8b52-168b-4b39-a227-4d6b4f102a56"


@pytest.fixture
def recording_api():
    return FishjamClient(FISHJAM_ID, FISHJAM_MANAGEMENT_TOKEN)


def mock_request(status_code: int, json_body):
    captured_requests = []

    def mock_send(request, **kwargs):
        captured_requests.append(request)
        return httpx.Response(status_code, json=json_body, request=request)

    return captured_requests, patch.object(
        httpx.HTTPTransport, "handle_request", side_effect=mock_send
    )


class TestGetAllRecordings:
    def test_returns_list(self, recording_api: FishjamClient):
        recordings = recording_api.get_all_recordings()

        assert isinstance(recordings, list)

    def test_unauthorized(self):
        recording_api = FishjamClient(FISHJAM_ID, "invalid")

        with pytest.raises(UnauthorizedError):
            recording_api.get_all_recordings()

    def test_metadata_filter_uses_deep_object_format(
        self, recording_api: FishjamClient
    ):
        captured_requests, request_patch = mock_request(200, {"data": []})

        with request_patch:
            recording_api.get_all_recordings(metadata={"env": "prod"})

        assert len(captured_requests) == 1
        params = captured_requests[0].url.params
        assert params.get("metadata[env]") == "prod"

    def test_metadata_filter_supports_nested_keys_and_none(
        self, recording_api: FishjamClient
    ):
        captured_requests, request_patch = mock_request(200, {"data": []})

        with request_patch:
            recording_api.get_all_recordings(metadata={"a": {"b": "c"}, "env": None})

        params = captured_requests[0].url.params
        assert params.get("metadata[a][b]") == "c"
        # values are compared as JSON strings by the API, so None must be
        # sent as "null" instead of being dropped from the query
        assert params.get("metadata[env]") == "null"

    def test_service_unavailable(self, recording_api: FishjamClient):
        _, request_patch = mock_request(503, {"errors": "service unavailable"})

        with request_patch, pytest.raises(ServiceUnavailableError):
            recording_api.get_all_recordings()


class TestCreateRecording:
    def test_returns_created_recording(self, recording_api: FishjamClient):
        source = CompositionSource(
            composition_url="https://example.com/composition",
            output_id="output-1",
        )
        recording_json = {
            "id": NONEXISTENT_RECORDING_ID,
            "source": source.to_dict(),
            "status": "active",
            "metadata": {"env": "test"},
        }
        captured_requests, request_patch = mock_request(201, {"data": recording_json})

        with request_patch:
            recording = recording_api.create_recording(source, metadata={"env": "test"})

        assert isinstance(recording, Recording)
        assert recording.id == NONEXISTENT_RECORDING_ID
        assert recording.status == RecordingStatus.ACTIVE

        assert len(captured_requests) == 1
        request = captured_requests[0]
        assert request.method == "POST"
        assert request.url.path.endswith("/recordings")
        assert json.loads(request.content) == {
            "source": source.to_dict(),
            "metadata": {"env": "test"},
        }

    def test_quota_exceeded(self, recording_api: FishjamClient):
        source = CompositionSource(
            composition_url="https://example.com/composition",
            output_id="output-1",
        )
        _, request_patch = mock_request(402, {"errors": "quota exceeded"})

        with request_patch, pytest.raises(QuotaExceededError):
            recording_api.create_recording(source)


class TestGetRecording:
    def test_id_not_found(self, recording_api: FishjamClient):
        with pytest.raises(NotFoundError):
            recording_api.get_recording(NONEXISTENT_RECORDING_ID)


class TestStopRecording:
    def test_id_not_found(self, recording_api: FishjamClient):
        with pytest.raises(NotFoundError):
            recording_api.stop_recording(NONEXISTENT_RECORDING_ID)


class TestDeleteRecording:
    def test_nonexistent_id_is_noop(self, recording_api: FishjamClient):
        recording_api.delete_recording(NONEXISTENT_RECORDING_ID)

    def test_server_error_raises(self, recording_api: FishjamClient):
        _, request_patch = mock_request(500, {"errors": "internal error"})

        with request_patch, pytest.raises(InternalServerError):
            recording_api.delete_recording(NONEXISTENT_RECORDING_ID)
