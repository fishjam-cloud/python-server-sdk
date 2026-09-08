from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

import httpx
import pytest

from fishjam import CompositionClient
from fishjam.composition import (
    AudioScene,
    CreateCompositionRequest,
    OutputWhipAudioOptions,
    OutputWhipVideoOptions,
    Resolution,
    VideoScene,
    View,
    ViewType,
    WhipOutput,
    WhipOutputType,
)
from fishjam.errors import (
    BadRequestError,
    CompositionNotFoundError,
    InputNotFoundError,
    InternalServerError,
    OutputNotFoundError,
    QuotaExceededError,
    RendererNotFoundError,
)
from fishjam.utils import get_composition_url

COMPOSITION_ID = "comp-1"
INPUT_ID = "cam"
OUTPUT_ID = "out-1"
IMAGE_ID = "logo"
LOCAL_URL = "http://localhost:8000"
FONT_PATH = Path(__file__).parent / "fixtures" / "font.ttf"


def client(composition_url: str | None = None) -> CompositionClient:
    return CompositionClient(management_token="token", composition_url=composition_url)


@contextmanager
def mock_response(body: dict | None = None, status: int = 200):
    requests: list[httpx.Request] = []

    def handle_request(request: httpx.Request, **_kwargs):
        request.read()
        requests.append(request)
        return httpx.Response(status, json=body if body is not None else {})

    with patch.object(
        httpx.HTTPTransport, "handle_request", side_effect=handle_request
    ):
        yield requests


def sent_json(requests: list[httpx.Request]) -> dict:
    import json

    return json.loads(requests[0].content)


class TestCompositionUrl:
    def test_defaults_to_the_production_composition_api(self):
        assert get_composition_url() == "https://rtc.fishjam.io"

    def test_uses_the_configured_address(self):
        assert get_composition_url(LOCAL_URL) == LOCAL_URL

    def test_keeps_the_origin_only_so_paths_are_not_doubled(self):
        assert get_composition_url(f"{LOCAL_URL}/") == LOCAL_URL

    def test_addresses_a_composition_on_the_configured_deployment(self):
        assert (
            client(LOCAL_URL).composition_url(COMPOSITION_ID)
            == f"{LOCAL_URL}/api/composition/comp-1"
        )

    def test_addresses_a_composition_on_production_by_default(self):
        assert (
            client().composition_url(COMPOSITION_ID)
            == "https://rtc.fishjam.io/api/composition/comp-1"
        )


class TestCompositionLifecycle:
    def test_creates_a_composition_with_the_default_config(self):
        with mock_response(
            {"composition_id": "comp-1", "api_url": LOCAL_URL}, status=201
        ) as requests:
            composition = client().create_composition()

        assert requests[0].url.path == "/api/composition"
        assert sent_json(requests) == {
            "autostart": True,
            "cleanup_without_inputs": True,
        }
        assert composition.composition_id == "comp-1"

    def test_creates_a_composition_that_waits_to_be_started(self):
        with mock_response(
            {"composition_id": "comp-1", "api_url": LOCAL_URL}, status=201
        ) as requests:
            client().create_composition(CreateCompositionRequest(autostart=False))

        assert sent_json(requests)["autostart"] is False

    def test_starts_a_composition(self):
        with mock_response() as requests:
            client().start_composition(COMPOSITION_ID)

        assert requests[0].method == "POST"
        assert requests[0].url.path == "/api/composition/comp-1/start"

    def test_resets_a_composition(self):
        with mock_response() as requests:
            client().reset_composition(COMPOSITION_ID)

        assert requests[0].method == "POST"
        assert requests[0].url.path == "/api/composition/comp-1/reset"

    def test_deletes_a_composition(self):
        with mock_response() as requests:
            client().delete_composition(COMPOSITION_ID)

        assert requests[0].method == "DELETE"
        assert requests[0].url.path == "/api/composition/comp-1"

    def test_reports_an_unparseable_success_rather_than_returning_nothing(self):
        with mock_response({"composition_id": "comp-1", "api_url": LOCAL_URL}):
            with pytest.raises(InternalServerError):
                client().create_composition()

    def test_requests_a_keyframe_from_an_output(self):
        with mock_response() as requests:
            client().request_keyframe(COMPOSITION_ID, OUTPUT_ID)

        assert requests[0].method == "POST"
        assert (
            requests[0].url.path
            == "/api/composition/comp-1/output/out-1/request_keyframe"
        )


class TestInputVariants:
    def test_resolves_the_whip_address_from_the_route_the_server_returned(self):
        with mock_response({
            "bearer_token": "tok",
            "endpoint_route": "/whip/server-chosen-route",
        }):
            target = client(LOCAL_URL).register_whip_input(COMPOSITION_ID, INPUT_ID)

        assert target.url == (
            f"{LOCAL_URL}/api/composition/comp-1/whip/server-chosen-route"
        )
        assert target.bearer_token == "tok"

    def test_falls_back_to_the_conventional_whip_route(self):
        with mock_response({"bearer_token": "tok"}):
            target = client(LOCAL_URL).register_whip_input(COMPOSITION_ID, INPUT_ID)

        assert target.url == f"{LOCAL_URL}/api/composition/comp-1/whip/cam"

    def test_url_encodes_the_input_id_in_the_fallback_route(self):
        with mock_response({"bearer_token": "tok"}):
            target = client(LOCAL_URL).register_whip_input(COMPOSITION_ID, "front cam")

        assert target.url == f"{LOCAL_URL}/api/composition/comp-1/whip/front%20cam"

    def test_keeps_a_caller_supplied_whip_token(self):
        with mock_response({"endpoint_route": "/whip/cam"}):
            target = client().register_whip_input(
                COMPOSITION_ID, INPUT_ID, bearer_token="mine"
            )

        assert target.bearer_token == "mine"

    def test_raises_when_no_whip_token_is_available(self):
        with mock_response({"endpoint_route": "/whip/cam"}):
            with pytest.raises(InternalServerError):
                client().register_whip_input(COMPOSITION_ID, INPUT_ID)

    def test_sends_the_whip_discriminant(self):
        with mock_response({"bearer_token": "tok"}) as requests:
            client().register_whip_input(COMPOSITION_ID, INPUT_ID, video=True)

        assert sent_json(requests) == {"type": "whip_server", "video": True}

    def test_sends_the_whep_discriminant(self):
        with mock_response() as requests:
            client().register_whep_input(
                COMPOSITION_ID, INPUT_ID, endpoint_url="https://example.com/whep"
            )

        assert sent_json(requests) == {
            "type": "whep_client",
            "endpoint_url": "https://example.com/whep",
        }

    def test_sends_the_mp4_discriminant(self):
        with mock_response() as requests:
            client().register_mp4_input(
                COMPOSITION_ID, INPUT_ID, url="https://example.com/a.mp4"
            )

        assert sent_json(requests) == {
            "type": "mp4",
            "url": "https://example.com/a.mp4",
        }

    def test_sends_the_rtmp_discriminant(self):
        with mock_response() as requests:
            client().register_rtmp_input(COMPOSITION_ID, INPUT_ID, stream_key="key")

        assert sent_json(requests) == {"type": "rtmp_server", "stream_key": "key"}

    def test_returns_the_durations_of_an_mp4_input(self):
        with mock_response({"video_duration_ms": 1000, "audio_duration_ms": 2000}):
            durations = client().register_mp4_input(
                COMPOSITION_ID, INPUT_ID, url="https://example.com/a.mp4"
            )

        assert durations.video_duration_ms == 1000
        assert durations.audio_duration_ms == 2000

    def test_leaves_unknown_mp4_durations_empty(self):
        with mock_response():
            durations = client().register_mp4_input(
                COMPOSITION_ID, INPUT_ID, url="https://example.com/a.mp4"
            )

        assert durations.video_duration_ms is None
        assert durations.audio_duration_ms is None


class TestOutputVariants:
    def test_sends_the_whip_discriminant(self):
        with mock_response() as requests:
            client().register_whip_output(
                COMPOSITION_ID, OUTPUT_ID, endpoint_url="https://example.com/whip"
            )

        assert sent_json(requests) == {
            "type": "whip_client",
            "endpoint_url": "https://example.com/whip",
        }

    def test_sends_the_rtmp_discriminant(self):
        with mock_response() as requests:
            client().register_rtmp_output(
                COMPOSITION_ID, OUTPUT_ID, url="rtmp://example.com/live"
            )

        assert sent_json(requests) == {
            "type": "rtmp_client",
            "url": "rtmp://example.com/live",
        }

    def test_carries_the_scenes_of_a_whip_output(self):
        with mock_response() as requests:
            client().register_whip_output(
                COMPOSITION_ID,
                OUTPUT_ID,
                endpoint_url="https://example.com/whip",
                video=OutputWhipVideoOptions(
                    resolution=Resolution(width=1280, height=720),
                    initial=VideoScene(root=View(type_=ViewType.VIEW)),
                ),
                audio=OutputWhipAudioOptions(initial=AudioScene(inputs=[])),
            )

        assert sent_json(requests) == {
            "type": "whip_client",
            "endpoint_url": "https://example.com/whip",
            "video": {
                "resolution": {"width": 1280, "height": 720},
                "initial": {"root": {"type": "view"}},
            },
            "audio": {"initial": {"inputs": []}},
        }

    def test_sends_a_prebuilt_output_as_it_is(self):
        output = WhipOutput(
            type_=WhipOutputType.WHIP_CLIENT,
            endpoint_url="https://example.com/whip",
            video=OutputWhipVideoOptions(
                resolution=Resolution(width=1280, height=720),
                initial=VideoScene(root=View(type_=ViewType.VIEW)),
            ),
        )

        with mock_response() as requests:
            client().register_output(COMPOSITION_ID, OUTPUT_ID, output)

        assert sent_json(requests) == {
            "type": "whip_client",
            "endpoint_url": "https://example.com/whip",
            "video": {
                "resolution": {"width": 1280, "height": 720},
                "initial": {"root": {"type": "view"}},
            },
        }


class TestFileUploads:
    def test_reads_a_font_from_a_path(self):
        with mock_response() as requests:
            client().register_font(COMPOSITION_ID, FONT_PATH)

        assert b"font-bytes" in requests[0].content
        assert b'filename="font.ttf"' in requests[0].content

    def test_uploads_a_font_as_a_file_not_a_form_field(self):
        with mock_response() as requests:
            client().register_font(COMPOSITION_ID, b"inline")

        assert b'name="font"; filename=' in requests[0].content

    def test_accepts_font_bytes_as_they_are(self):
        with mock_response() as requests:
            client().register_font(COMPOSITION_ID, b"inline")

        assert b"inline" in requests[0].content

    def test_uploads_a_template_bundle_alongside_its_output_config(self):
        output = WhipOutput(
            type_=WhipOutputType.WHIP_CLIENT,
            endpoint_url="https://example.com/whip",
        )

        with mock_response() as requests:
            client().register_template_output(
                COMPOSITION_ID, OUTPUT_ID, output, b"bundle"
            )

        content = requests[0].content
        assert b"bundle" in content
        assert b'name="template"; filename=' in content
        assert b'"whip_client"' in content


class TestMissingResources:
    def test_reports_a_missing_input_rather_than_a_missing_composition(self):
        with mock_response({"message": "gone"}, status=404):
            with pytest.raises(InputNotFoundError):
                client().unregister_input(COMPOSITION_ID, INPUT_ID)

    def test_reports_a_missing_output_rather_than_a_missing_composition(self):
        with mock_response({"message": "gone"}, status=404):
            with pytest.raises(OutputNotFoundError):
                client().unregister_output(COMPOSITION_ID, OUTPUT_ID)

    def test_reports_a_missing_image_rather_than_a_missing_composition(self):
        with mock_response({"message": "gone"}, status=404):
            with pytest.raises(RendererNotFoundError):
                client().unregister_image(COMPOSITION_ID, IMAGE_ID)

    def test_reports_a_missing_composition_everywhere_else(self):
        with mock_response({"message": "gone"}, status=404):
            with pytest.raises(CompositionNotFoundError):
                client().start_composition(COMPOSITION_ID)

    def test_maps_a_status_outside_the_standard_set(self):
        with mock_response({"message": "gateway"}, status=520):
            with pytest.raises(InternalServerError):
                client().create_composition()

    def test_carries_the_server_message_as_text(self):
        with mock_response({"message": "gone"}, status=404):
            with pytest.raises(InputNotFoundError) as raised:
                client().unregister_input(COMPOSITION_ID, INPUT_ID)

        assert str(raised.value) == "gone"

    def test_maps_a_payment_required_to_a_quota_error(self):
        with mock_response({"message": "over quota"}, status=402):
            with pytest.raises(QuotaExceededError):
                client().create_composition()

    def test_maps_an_unprocessable_request_to_a_bad_request(self):
        with mock_response({"message": "nope"}, status=422):
            with pytest.raises(BadRequestError):
                client().send_event(COMPOSITION_ID, "scene", {"layout": "grid"})


class TestUpdateOutput:
    def test_sends_both_scenes_so_the_update_mirrors_the_registration(self):
        with mock_response() as requests:
            client().update_output(
                COMPOSITION_ID,
                OUTPUT_ID,
                video=VideoScene(root=View(type_=ViewType.VIEW)),
                audio=AudioScene(inputs=[]),
            )

        assert sent_json(requests) == {
            "video": {"root": {"type": "view"}},
            "audio": {"inputs": []},
        }


class TestPublicModels:
    ENVELOPES = {
        "ApiError",
        "EmptyResponse",
        "RegisterFontBody",
        "RegisterTemplateOutputBody",
        "SendCompositionEventBody",
    }

    ALIASES = {"FileSource", "ImageSpec", "RegisterInput", "RegisterOutput"}

    def test_exports_every_model_except_the_wire_envelopes(self):
        import fishjam.composition as public
        from fishjam._composition_openapi_client import models as generated

        assert set(public.__all__) == (
            set(generated.__all__) - self.ENVELOPES | self.ALIASES
        )

    def test_exports_the_unions_its_public_methods_declare(self):
        import fishjam.composition as public

        assert self.ALIASES <= set(dir(public))

    def test_keeps_the_request_bodies_the_client_builds_itself_private(self):
        import fishjam.composition as public

        assert not self.ENVELOPES & set(dir(public))
