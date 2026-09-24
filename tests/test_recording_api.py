import json
from unittest.mock import patch

import httpx
import pytest

from fishjam import FishjamClient, Recording
from fishjam.errors import (
    BadRequestError,
    InternalServerError,
    NotFoundError,
    QuotaExceededError,
    ServiceUnavailableError,
    UnauthorizedError,
)
from fishjam.recording import (
    CompositionSource,
    RecordingSource,
    RecordingStatus,
    TemplateSource,
    TemplateSourceResolution,
)
from tests.support.env import FISHJAM_ID, FISHJAM_MANAGEMENT_TOKEN

NONEXISTENT_RECORDING_ID = "515c8b52-168b-4b39-a227-4d6b4f102a56"
RECORDING_ID = "8e9b40aa-27d5-4e05-b6c1-27eb85f603f7"


@pytest.fixture
def recording_api():
    return FishjamClient(FISHJAM_ID, FISHJAM_MANAGEMENT_TOKEN)


def make_composition_source():
    return CompositionSource(
        composition_url="https://example.com/composition",
        output_id="output-1",
    )


def make_template_source():
    return TemplateSource(composition_url="https://example.com/composition")


def make_recording_json(source: RecordingSource, status: str):
    return {
        "id": RECORDING_ID,
        "files": [],
        "source": source.to_dict(),
        "status": status,
    }


def mock_request(status_code: int, json_body):
    captured_requests = []

    def mock_send(request, **kwargs):
        request.read()
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
        source = make_composition_source()
        recording_json = make_recording_json(source, "active")
        recording_json["metadata"] = {"env": "test"}
        captured_requests, request_patch = mock_request(201, {"data": recording_json})

        with request_patch:
            recording = recording_api.create_recording(source, metadata={"env": "test"})

        assert isinstance(recording, Recording)
        assert recording.id == RECORDING_ID
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
        _, request_patch = mock_request(402, {"errors": "quota exceeded"})

        with request_patch, pytest.raises(QuotaExceededError):
            recording_api.create_recording(make_composition_source())


class TestCreateTemplateRecording:
    def test_uploads_the_bundle_alongside_the_config(
        self, recording_api: FishjamClient
    ):
        source = make_template_source()
        recording_json = make_recording_json(source, "active")
        recording_json["metadata"] = {"env": "test"}
        captured_requests, request_patch = mock_request(201, {"data": recording_json})

        with request_patch:
            recording = recording_api.create_template_recording(
                source, b"bundle", metadata={"env": "test"}
            )

        assert isinstance(recording, Recording)
        assert recording.id == RECORDING_ID
        assert recording.status == RecordingStatus.ACTIVE

        assert len(captured_requests) == 1
        request = captured_requests[0]
        assert request.method == "POST"
        assert request.url.path.endswith("/recordings")
        assert request.headers["content-type"].startswith(
            "multipart/form-data; boundary="
        )

        content = request.content
        assert b'name="config"' in content
        assert (
            json.dumps({
                "source": source.to_dict(),
                "metadata": {"env": "test"},
            }).encode()
            in content
        )
        assert b'name="template"; filename=' in content
        assert b"bundle" in content

    def test_reads_the_bundle_from_a_path(self, recording_api: FishjamClient, tmp_path):
        source = make_template_source()
        bundle = tmp_path / "index.js"
        bundle.write_bytes(b"bundle-from-a-file")
        captured_requests, request_patch = mock_request(
            201, {"data": make_recording_json(source, "active")}
        )

        with request_patch:
            recording_api.create_template_recording(source, bundle)

        content = captured_requests[0].content
        assert b"bundle-from-a-file" in content
        assert b'filename="index.js"' in content

    def test_returns_a_recording_rendering_its_own_scene(
        self, recording_api: FishjamClient
    ):
        source = TemplateSource(
            composition_url="https://example.com/composition",
            resolution=TemplateSourceResolution(width=1920, height=1080),
            audio=False,
        )
        recording_json = make_recording_json(source, "available")
        _, request_patch = mock_request(200, {"data": recording_json})

        with request_patch:
            recording = recording_api.get_recording(RECORDING_ID)

        assert isinstance(recording, Recording)
        assert recording.source == source

    def test_rejected_bundle_raises(self, recording_api: FishjamClient):
        _, request_patch = mock_request(400, {"errors": "template bundle is invalid"})

        with request_patch, pytest.raises(BadRequestError):
            recording_api.create_template_recording(make_template_source(), b"bundle")


class TestGetRecording:
    def test_returns_recording(self, recording_api: FishjamClient):
        source = make_composition_source()
        recording_json = make_recording_json(source, "available")
        captured_requests, request_patch = mock_request(200, {"data": recording_json})

        with request_patch:
            recording = recording_api.get_recording(RECORDING_ID)

        assert isinstance(recording, Recording)
        assert recording.id == RECORDING_ID
        assert recording.status == RecordingStatus.AVAILABLE
        assert recording.source == source

        request = captured_requests[0]
        assert request.method == "GET"
        assert request.url.path.endswith(f"/recordings/{RECORDING_ID}")

    def test_id_not_found(self, recording_api: FishjamClient):
        with pytest.raises(NotFoundError):
            recording_api.get_recording(NONEXISTENT_RECORDING_ID)


class TestStopRecording:
    def test_returns_stopped_recording(self, recording_api: FishjamClient):
        source = make_composition_source()
        # the recording stays `active` until finalization completes
        recording_json = make_recording_json(source, "active")
        captured_requests, request_patch = mock_request(200, {"data": recording_json})

        with request_patch:
            recording = recording_api.stop_recording(RECORDING_ID)

        assert isinstance(recording, Recording)
        assert recording.id == RECORDING_ID
        assert recording.status == RecordingStatus.ACTIVE

        request = captured_requests[0]
        assert request.method == "POST"
        assert request.url.path.endswith(f"/recordings/{RECORDING_ID}/stop")

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
