from unittest.mock import MagicMock, patch

import pytest
from google.genai import types

from fishjam.integrations.gemini import GeminiIntegration
from fishjam.version import get_version


@pytest.fixture
def version():
    return get_version()


@patch("google.genai.Client")
def test_create_client_passes_all_args(mock_client_cls: MagicMock, version: str):
    dummy_credentials = MagicMock()
    dummy_debug_config = MagicMock()

    GeminiIntegration.create_client(
        vertexai=True,
        api_key="test-key",
        credentials=dummy_credentials,
        project="my-project",
        location="us-central1",
        debug_config=dummy_debug_config,
    )

    mock_client_cls.assert_called_once()

    kwargs = mock_client_cls.call_args.kwargs

    assert kwargs["vertexai"] is True
    assert kwargs["api_key"] == "test-key"
    assert kwargs["credentials"] is dummy_credentials
    assert kwargs["project"] == "my-project"
    assert kwargs["location"] == "us-central1"
    assert kwargs["debug_config"] is dummy_debug_config

    assert kwargs["http_options"] == {
        "headers": {"x-goog-api-client": f"fishjam-python-server-sdk/{version}"}
    }


@patch("google.genai.Client")
def test_create_client_with_dict_options_no_headers(
    mock_client_cls: MagicMock, version: str
):
    GeminiIntegration.create_client(http_options={"timeout": 30})

    mock_client_cls.assert_called_once()

    assert mock_client_cls.call_args.kwargs["http_options"] == {
        "timeout": 30,
        "headers": {"x-goog-api-client": f"fishjam-python-server-sdk/{version}"},
    }


@patch("google.genai.Client")
def test_create_client_with_dict_options_existing_headers(
    mock_client_cls: MagicMock, version: str
):
    GeminiIntegration.create_client(
        http_options={
            "headers": {
                "existing-header": "value",
                "x-goog-api-client": "other",
            }
        }
    )

    mock_client_cls.assert_called_once()

    assert mock_client_cls.call_args.kwargs["http_options"] == {
        "headers": {
            "existing-header": "value",
            "x-goog-api-client": f"fishjam-python-server-sdk/{version}",
        },
    }


@patch("google.genai.Client")
def test_create_client_with_object_options(mock_client_cls: MagicMock, version: str):
    http_options = types.HttpOptions()

    GeminiIntegration.create_client(http_options=http_options)

    mock_client_cls.assert_called_once()

    # Verify the object passed has the correct headers set
    actual_options = mock_client_cls.call_args.kwargs["http_options"]
    assert actual_options.headers == {
        "x-goog-api-client": f"fishjam-python-server-sdk/{version}"
    }


@patch("google.genai.Client")
def test_create_client_with_object_options_existing_headers(
    mock_client_cls: MagicMock, version: str
):
    http_options = types.HttpOptions(
        headers={
            "user-header": "123",
            "x-goog-api-client": "other",
        }
    )

    GeminiIntegration.create_client(http_options=http_options)

    mock_client_cls.assert_called_once()

    actual_options = mock_client_cls.call_args.kwargs["http_options"]
    assert actual_options.headers == {
        "user-header": "123",
        "x-goog-api-client": f"fishjam-python-server-sdk/{version}",
    }
