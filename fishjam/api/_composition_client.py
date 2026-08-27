"""Composition client used to manage compositions, the video compositing sessions."""

from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Any, TypeVar, cast
from urllib.parse import quote

from fishjam._composition_openapi_client.api.compositions import (
    create_composition as compositions_create,
)
from fishjam._composition_openapi_client.api.compositions import (
    delete_composition as compositions_delete,
)
from fishjam._composition_openapi_client.api.compositions import (
    reset as compositions_reset,
)
from fishjam._composition_openapi_client.api.compositions import (
    start as compositions_start,
)
from fishjam._composition_openapi_client.api.events import (
    send_composition_event as events_send,
)
from fishjam._composition_openapi_client.api.inputs import (
    register_input as inputs_register,
)
from fishjam._composition_openapi_client.api.inputs import (
    unregister_input as inputs_unregister,
)
from fishjam._composition_openapi_client.api.outputs import (
    register_output as outputs_register,
)
from fishjam._composition_openapi_client.api.outputs import (
    register_template_output as outputs_register_template,
)
from fishjam._composition_openapi_client.api.outputs import (
    request_keyframe as outputs_request_keyframe,
)
from fishjam._composition_openapi_client.api.outputs import (
    unregister_output as outputs_unregister,
)
from fishjam._composition_openapi_client.api.outputs import (
    update_output as outputs_update,
)
from fishjam._composition_openapi_client.api.renderers import (
    register_font as renderers_register_font,
)
from fishjam._composition_openapi_client.api.renderers import (
    register_image as renderers_register_image,
)
from fishjam._composition_openapi_client.api.renderers import (
    unregister_image as renderers_unregister_image,
)
from fishjam._composition_openapi_client.client import AuthenticatedClient
from fishjam._composition_openapi_client.errors import UnexpectedStatus
from fishjam._composition_openapi_client.models import (
    ApiError,
    AudioScene,
    CompositionCreatedResponse,
    CreateCompositionRequest,
    Mp4Input,
    Mp4InputType,
    OutputRtmpClientAudioOptions,
    OutputRtmpClientVideoOptions,
    OutputWhipAudioOptions,
    OutputWhipVideoOptions,
    RegisterFontBody,
    RegisterInputResponse,
    RegisterTemplateOutputBody,
    RtmpInput,
    RtmpInputType,
    RtmpOutput,
    RtmpOutputType,
    SendCompositionEventBody,
    UnregisterInput,
    UnregisterOutput,
    UnregisterRenderer,
    UpdateOutputRequest,
    VideoScene,
    WhepInput,
    WhepInputType,
    WhipInput,
    WhipInputType,
    WhipOutput,
    WhipOutputType,
)
from fishjam._composition_openapi_client.types import UNSET, File, Unset
from fishjam.composition import (
    FileSource,
    ImageSpec,
    RegisterInput,
    RegisterOutput,
)
from fishjam.errors import (
    CompositionNotFoundError,
    HTTPError,
    InputNotFoundError,
    InternalServerError,
    OutputNotFoundError,
    RendererNotFoundError,
    error_for_status,
)
from fishjam.utils import get_composition_url
from fishjam.version import get_version

T = TypeVar("T")


@dataclass
class WhipInputTarget:
    """Where to publish a WHIP input.

    The input is registered with `CompositionClient.register_whip_input`. Hand
    these to a WHIP publisher, such as `useLivestreamStreamer` in the React
    client SDK.

    Attributes:
        url: Address to publish to.
        bearer_token: Token authorizing the publisher.
    """

    url: str
    """Address to publish to"""
    bearer_token: str
    """Token authorizing the publisher"""


@dataclass
class Mp4InputDurations:
    """How much media an MP4 input holds.

    The input is registered with `CompositionClient.register_mp4_input`.

    Attributes:
        video_duration_ms: Length of the video track, when the file has one.
        audio_duration_ms: Length of the audio track, when the file has one.
    """

    video_duration_ms: int | None
    """Length of the video track, when the file has one"""
    audio_duration_ms: int | None
    """Length of the audio track, when the file has one"""


def _to_error(
    status_code: int, error: ApiError | None, not_found: type[HTTPError]
) -> HTTPError:
    """Turn a failed Composition API response into the matching Fishjam error.

    Args:
        status_code: Status the Composition API responded with.
        error: Parsed error body, when the response carried one.
        not_found: Error class describing the resource a 404 refers to.

    Returns:
        The error to raise.
    """
    return error_for_status(status_code, error.message if error else "", not_found)


def _to_file(source: FileSource, name: str) -> File:
    """Read an upload from bytes or from a path.

    The upload is named, so it is sent as a file rather than a plain form field.
    Never pass a path taken from untrusted input, since its contents are uploaded.

    Args:
        source: The bytes to upload, or a path to read them from.
        name: Name to send the upload under, when the source has none of its own.

    Returns:
        The upload, as the generated client takes it.
    """
    if isinstance(source, bytes):
        return File(payload=BytesIO(source), file_name=name)

    path = Path(source)

    return File(payload=BytesIO(path.read_bytes()), file_name=path.name)


class CompositionClient:
    """Client class that allows to manage compositions.

    A composition is a real-time video compositing session of a Fishjam App. It
    requires the management token that can be retrieved from the Fishjam Dashboard,
    the same one used by `fishjam.FishjamClient`.

    Example usage:
    ```python
    client = CompositionClient(management_token="your-management-token")
    ```
    """

    def __init__(self, management_token: str, composition_url: str | None = None):
        """Create a client talking to the Composition API.

        Args:
            management_token: Secret token authorizing to perform actions on your
                account. It is the same token `fishjam.FishjamClient` is configured
                with. Never share this token with anyone.
            composition_url: Address of the Composition API. Only needs setting when
                running against a deployment other than production.
        """
        self._url = get_composition_url(composition_url)
        self.client = AuthenticatedClient(
            self._url,
            token=management_token,
            headers={"x-fishjam-api-client": f"python-server/{get_version()}"},
            raise_on_unexpected_status=True,
        )

    def _request(
        self,
        method,
        not_found: type[HTTPError] = CompositionNotFoundError,
        **kwargs,
    ):
        try:
            response = method.sync_detailed(client=self.client, **kwargs)
        except UnexpectedStatus as status:
            raise error_for_status(
                status.status_code,
                status.content.decode(errors="replace"),
                not_found,
            ) from status
        except ValueError as error:
            raise InternalServerError(
                f"The Composition API answered with a status the client cannot "
                f"interpret: {error}"
            ) from error

        if isinstance(response.parsed, ApiError):
            raise _to_error(response.status_code, response.parsed, not_found)

        return response.parsed

    def composition_url(self, composition_id: str) -> str:
        """The address of a composition, as other services refer to it.

        Fishjam needs it to forward a room's tracks with
        `fishjam.FishjamClient.forward_room_tracks`.

        Args:
            composition_id: ID of the composition.

        Returns:
            The address of the composition.
        """
        return f"{self._url}/api/composition/{composition_id}"

    def create_composition(
        self, config: CreateCompositionRequest | None = None
    ) -> CompositionCreatedResponse:
        """Create a new composition.

        Inputs registered on it are composed into the scenes its outputs render.

        Args:
            config: Configuration of the composition.

        Returns:
            The created composition.
        """
        return cast(
            CompositionCreatedResponse,
            self._request(
                compositions_create, body=config or CreateCompositionRequest()
            ),
        )

    def start_composition(self, composition_id: str) -> None:
        """Start a composition created with `autostart` disabled.

        Its outputs begin producing audio and video.

        Args:
            composition_id: ID of the composition.
        """
        self._request(compositions_start, composition_id=composition_id)

    def reset_composition(self, composition_id: str) -> None:
        """Reset a composition, tearing down its scene but keeping it alive.

        Args:
            composition_id: ID of the composition.
        """
        self._request(compositions_reset, composition_id=composition_id)

    def delete_composition(self, composition_id: str) -> None:
        """Delete an existing composition. Its inputs and outputs are torn down with it.

        Args:
            composition_id: ID of the composition.
        """
        self._request(compositions_delete, composition_id=composition_id)

    def register_input(
        self,
        composition_id: str,
        input_id: str,
        input_: RegisterInput,
    ) -> RegisterInputResponse:
        """Register a media source on a composition.

        Prefer the variant methods, such as
        `CompositionClient.register_whip_input`, which return what that input
        type produces.

        Args:
            composition_id: ID of the composition.
            input_id: ID to register the input under.
            input_: Configuration of the input.

        Returns:
            Whatever the input type produces on registration.
        """
        return cast(
            RegisterInputResponse,
            self._request(
                inputs_register,
                composition_id=composition_id,
                input_id=input_id,
                body=input_,
            ),
        )

    def register_whip_input(
        self,
        composition_id: str,
        input_id: str,
        *,
        bearer_token: str | None = None,
        video: bool | None = None,
    ) -> WhipInputTarget:
        """Register an input that a WHIP publisher pushes media into.

        Args:
            composition_id: ID of the composition.
            input_id: ID to register the input under.
            bearer_token: Token the publisher authenticates with. The server picks one
                when it is not given.
            video: Whether the input accepts an h264-encoded video track.

        Returns:
            The address and token to publish with.

        Raises:
            InternalServerError: When neither the caller nor the server provides a
                token, leaving the input impossible to publish to.
        """
        response = self.register_input(
            composition_id,
            input_id,
            WhipInput(
                type_=WhipInputType.WHIP_SERVER,
                bearer_token=_or_unset(bearer_token),
                video=_or_unset(video),
            ),
        )

        token = _or_none(response.bearer_token) or bearer_token
        if not token:
            raise InternalServerError(
                f'Registering WHIP input "{input_id}" returned no bearer token, '
                "so it cannot be published to"
            )

        route = _or_none(response.endpoint_route) or f"/whip/{quote(input_id, safe='')}"

        return WhipInputTarget(
            url=f"{self.composition_url(composition_id)}{route}", bearer_token=token
        )

    def register_whep_input(
        self,
        composition_id: str,
        input_id: str,
        *,
        endpoint_url: str,
        bearer_token: str | None = None,
        video: bool | None = None,
    ) -> None:
        """Register an input that pulls media from a WHEP endpoint.

        Args:
            composition_id: ID of the composition.
            input_id: ID to register the input under.
            endpoint_url: Address of the WHEP endpoint to pull from.
            bearer_token: Token to authenticate with.
            video: Whether the input accepts an h264-encoded video track.
        """
        self.register_input(
            composition_id,
            input_id,
            WhepInput(
                type_=WhepInputType.WHEP_CLIENT,
                endpoint_url=endpoint_url,
                bearer_token=_or_unset(bearer_token),
                video=_or_unset(video),
            ),
        )

    def register_mp4_input(
        self,
        composition_id: str,
        input_id: str,
        *,
        url: str,
        loop: bool | None = None,
    ) -> Mp4InputDurations:
        """Register an input that plays an MP4 file.

        Args:
            composition_id: ID of the composition.
            input_id: ID to register the input under.
            url: Address of the file to play.
            loop: Whether the file restarts when it ends.

        Returns:
            How much media the file holds.
        """
        response = self.register_input(
            composition_id,
            input_id,
            Mp4Input(type_=Mp4InputType.MP4, url=url, loop=_or_unset(loop)),
        )

        return Mp4InputDurations(
            video_duration_ms=_or_none(response.video_duration_ms),
            audio_duration_ms=_or_none(response.audio_duration_ms),
        )

    def register_rtmp_input(
        self, composition_id: str, input_id: str, *, stream_key: str
    ) -> None:
        """Register an input that an RTMP publisher pushes media into.

        The stream key identifies the input; the address to publish to belongs to the
        composition, not to this call.

        Args:
            composition_id: ID of the composition.
            input_id: ID to register the input under.
            stream_key: Key the publisher identifies the input with.
        """
        self.register_input(
            composition_id,
            input_id,
            RtmpInput(type_=RtmpInputType.RTMP_SERVER, stream_key=stream_key),
        )

    def unregister_input(
        self,
        composition_id: str,
        input_id: str,
        options: UnregisterInput | None = None,
    ) -> None:
        """Unregister an input. Scenes referencing it stop receiving its media.

        Args:
            composition_id: ID of the composition.
            input_id: ID of the input.
            options: When to unregister the input.
        """
        self._request(
            inputs_unregister,
            not_found=InputNotFoundError,
            composition_id=composition_id,
            input_id=input_id,
            body=options or UnregisterInput(),
        )

    def register_output(
        self, composition_id: str, output_id: str, output: RegisterOutput
    ) -> None:
        """Register an output, the destination the composed result is sent to.

        Args:
            composition_id: ID of the composition.
            output_id: ID to register the output under.
            output: Configuration of the output, carrying the scene to render.
        """
        self._request(
            outputs_register,
            composition_id=composition_id,
            output_id=output_id,
            body=output,
        )

    def register_template_output(
        self,
        composition_id: str,
        output_id: str,
        config: RegisterOutput,
        template: FileSource,
    ) -> None:
        """Register an output rendering a template bundle.

        The bundle is built by `@fishjam-cloud/composition-cli`. Never pass a path taken
        from untrusted input, since its contents are uploaded.

        A template rebuilds both scenes from React, so `video.initial` and
        `audio.initial` are ignored. Omitting `audio` entirely still means no audio
        track at all, so pass an audio option with an empty scene when the output
        should carry audio.

        Args:
            composition_id: ID of the composition.
            output_id: ID to register the output under.
            config: Configuration of the output.
            template: The bundle to render, as bytes or a path to read them from.
        """
        self._request(
            outputs_register_template,
            composition_id=composition_id,
            output_id=output_id,
            body=RegisterTemplateOutputBody(
                config=config, template=_to_file(template, "template.js")
            ),
        )

    def register_whip_output(
        self,
        composition_id: str,
        output_id: str,
        *,
        endpoint_url: str,
        bearer_token: str | None = None,
        video: OutputWhipVideoOptions | None = None,
        audio: OutputWhipAudioOptions | None = None,
    ) -> None:
        """Register an output sending the composed result to a WHIP endpoint.

        Args:
            composition_id: ID of the composition.
            output_id: ID to register the output under.
            endpoint_url: Address of the WHIP endpoint to publish to.
            bearer_token: Token to authenticate with.
            video: Video options, carrying the scene to render.
            audio: Audio options, carrying the scene to mix.
        """
        self.register_output(
            composition_id,
            output_id,
            WhipOutput(
                type_=WhipOutputType.WHIP_CLIENT,
                endpoint_url=endpoint_url,
                bearer_token=_or_unset(bearer_token),
                video=_or_unset(video),
                audio=_or_unset(audio),
            ),
        )

    def register_rtmp_output(
        self,
        composition_id: str,
        output_id: str,
        *,
        url: str,
        video: OutputRtmpClientVideoOptions | None = None,
        audio: OutputRtmpClientAudioOptions | None = None,
    ) -> None:
        """Register an output sending the composed result to an RTMP endpoint.

        Args:
            composition_id: ID of the composition.
            output_id: ID to register the output under.
            url: Address of the RTMP endpoint to publish to.
            video: Video options, carrying the scene to render.
            audio: Audio options, carrying the scene to mix.
        """
        self.register_output(
            composition_id,
            output_id,
            RtmpOutput(
                type_=RtmpOutputType.RTMP_CLIENT,
                url=url,
                video=_or_unset(video),
                audio=_or_unset(audio),
            ),
        )

    def unregister_output(
        self,
        composition_id: str,
        output_id: str,
        options: UnregisterOutput | None = None,
    ) -> None:
        """Unregister an output. It stops producing audio and video.

        Args:
            composition_id: ID of the composition.
            output_id: ID of the output.
            options: When to unregister the output.
        """
        self._request(
            outputs_unregister,
            not_found=OutputNotFoundError,
            composition_id=composition_id,
            output_id=output_id,
            body=options or UnregisterOutput(),
        )

    def update_output(
        self,
        composition_id: str,
        output_id: str,
        update: UpdateOutputRequest | None = None,
        *,
        video: VideoScene | None = None,
        audio: AudioScene | None = None,
    ) -> None:
        """Replace the scenes an output renders.

        An update has to mirror the registration: whatever the output was
        registered with, video, audio or both, has to be given here too, and
        whatever it was registered without cannot be.

        Args:
            composition_id: ID of the composition.
            output_id: ID of the output.
            update: The update to apply.
            video: The video scene to render, when no full update is given.
            audio: The audio scene to mix, when no full update is given.
        """
        self._request(
            outputs_update,
            composition_id=composition_id,
            output_id=output_id,
            body=update
            or UpdateOutputRequest(video=_or_unset(video), audio=_or_unset(audio)),
        )

    def request_keyframe(self, composition_id: str, output_id: str) -> None:
        """Ask an output to emit a keyframe.

        A viewer joining mid-stream then renders a full picture sooner.

        Args:
            composition_id: ID of the composition.
            output_id: ID of the output.
        """
        self._request(
            outputs_request_keyframe,
            composition_id=composition_id,
            output_id=output_id,
        )

    def register_image(
        self, composition_id: str, image_id: str, image: ImageSpec
    ) -> None:
        """Register an image that scenes can reference by its renderer ID.

        Args:
            composition_id: ID of the composition.
            image_id: ID to register the image under.
            image: Where to fetch the image from and how to decode it.
        """
        self._request(
            renderers_register_image,
            composition_id=composition_id,
            image_id=image_id,
            body=image,
        )

    def register_font(self, composition_id: str, font: FileSource) -> None:
        """Register a font that scenes can render text with.

        Never pass a path taken from untrusted input, since its contents are uploaded.

        Args:
            composition_id: ID of the composition.
            font: The font to upload, as bytes or a path to read them from.
        """
        self._request(
            renderers_register_font,
            composition_id=composition_id,
            body=RegisterFontBody(font=_to_file(font, "font")),
        )

    def unregister_image(
        self,
        composition_id: str,
        image_id: str,
        options: UnregisterRenderer | None = None,
    ) -> None:
        """Unregister a previously registered image.

        Args:
            composition_id: ID of the composition.
            image_id: ID of the image.
            options: When to unregister the image.
        """
        self._request(
            renderers_unregister_image,
            not_found=RendererNotFoundError,
            composition_id=composition_id,
            image_id=image_id,
            body=options or UnregisterRenderer(),
        )

    def send_event(
        self, composition_id: str, event_name: str, data: Any = None
    ) -> None:
        """Deliver an event to the templates rendered by the composition's outputs.

        Args:
            composition_id: ID of the composition.
            event_name: Name the template listens for.
            data: Payload the template receives with the event.
        """
        self._request(
            events_send,
            composition_id=composition_id,
            body=SendCompositionEventBody(event_name=event_name, data=_or_unset(data)),
        )


def _or_unset(value: T | None) -> T | Unset:
    return UNSET if value is None else value


def _or_none(value: T | Unset) -> T | None:
    return None if isinstance(value, Unset) else value
