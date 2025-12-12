try:
    from google import genai
    from google.auth.credentials import Credentials
    from google.genai import types
    from google.genai.client import DebugConfig
except ImportError:
    raise ImportError(
        "To use the Fishjam Gemini integration, you need to import the `gemini` extra."
        "Install it with `pip install 'fishjam-server-sdk[gemini]'`"
    )

from functools import singledispatch
from typing import Optional, Union

from fishjam import AgentOutputOptions
from fishjam.version import get_version


def _get_headers():
    return {"x-goog-api-client": f"fishjam-python-server-sdk/{get_version()}"}


@singledispatch
def _add_fishjam_header(
    http_options: Optional[Union[types.HttpOptions, types.HttpOptionsDict]],
) -> Union[types.HttpOptions, types.HttpOptionsDict]: ...


@_add_fishjam_header.register
def _(http_options: types.HttpOptions) -> types.HttpOptions:
    http_options.headers = (http_options.headers or {}) | _get_headers()
    return http_options


@_add_fishjam_header.register
def _(http_options: types.HttpOptionsDict) -> types.HttpOptionsDict:
    headers = (http_options.get("headers") or {}) | _get_headers()
    return http_options | {"headers": headers}


@_add_fishjam_header.register
def _(_http_options: None) -> types.HttpOptionsDict:
    return {"headers": _get_headers()}


class _GeminiIntegration:
    def create_client(
        self,
        vertexai: Optional[bool] = None,
        api_key: Optional[str] = None,
        credentials: Optional[Credentials] = None,
        project: Optional[str] = None,
        location: Optional[str] = None,
        debug_config: Optional[DebugConfig] = None,
        http_options: Optional[Union[types.HttpOptions, types.HttpOptionsDict]] = None,
    ):
        full_http_options = _add_fishjam_header(http_options)

        return genai.Client(
            vertexai=vertexai,
            api_key=api_key,
            credentials=credentials,
            project=project,
            location=location,
            debug_config=debug_config,
            http_options=full_http_options,
        )

    @property
    def GeminiInputAudioSettings(self) -> AgentOutputOptions:
        return AgentOutputOptions(
            audio_format="pcm16",
            audio_sample_rate=16_000,
        )


GeminiIntegration = _GeminiIntegration()
