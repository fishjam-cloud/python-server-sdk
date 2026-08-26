"""Fishjam client used to manage rooms."""

from dataclasses import dataclass, field
from http import HTTPStatus
from typing import Any, Literal, cast

from fishjam._openapi_client.api.credentials import (
    validate_credentials as credentials_validate_credentials,
)
from fishjam._openapi_client.api.mo_q import (
    create_moq_access as moq_create_access,
)
from fishjam._openapi_client.api.recordings import (
    create_recording as recording_create_recording,
)
from fishjam._openapi_client.api.recordings import (
    delete_recording as recording_delete_recording,
)
from fishjam._openapi_client.api.recordings import (
    get_recording as recording_get_recording,
)
from fishjam._openapi_client.api.recordings import (
    list_recordings as recording_list_recordings,
)
from fishjam._openapi_client.api.recordings import (
    stop_recording as recording_stop_recording,
)
from fishjam._openapi_client.api.rooms import add_peer as room_add_peer
from fishjam._openapi_client.api.rooms import create_room as room_create_room
from fishjam._openapi_client.api.rooms import delete_peer as room_delete_peer
from fishjam._openapi_client.api.rooms import delete_room as room_delete_room
from fishjam._openapi_client.api.rooms import get_all_rooms as room_get_all_rooms
from fishjam._openapi_client.api.rooms import get_room as room_get_room
from fishjam._openapi_client.api.rooms import refresh_token as room_refresh_token
from fishjam._openapi_client.api.rooms import subscribe_peer as room_subscribe_peer
from fishjam._openapi_client.api.rooms import subscribe_tracks as room_subscribe_tracks
from fishjam._openapi_client.api.streamers import (
    generate_streamer_token as streamer_generate_streamer_token,
)
from fishjam._openapi_client.api.track_forwardings import (
    create_track_forwarding as track_forwardings_create,
)
from fishjam._openapi_client.api.viewers import (
    generate_viewer_token as viewer_generate_viewer_token,
)
from fishjam._openapi_client.models import (
    AgentOutput,
    AudioFormat,
    AudioSampleRate,
    CompositionInfo,
    CompositionSource,
    ListRecordingsMetadata,
    MoqAccess,
    MoqAccessConfig,
    Peer,
    PeerConfigAgent,
    PeerConfigAgentType,
    PeerConfigVAPI,
    PeerConfigVAPIType,
    PeerConfigWebRTC,
    PeerConfigWebRTCType,
    PeerDetailsResponse,
    PeerOptionsAgent,
    PeerOptionsVapi,
    PeerOptionsWebRTC,
    PeerRefreshTokenResponse,
    Recording,
    RecordingConfig,
    RecordingConfigMetadataType0,
    RecordingDetailsResponse,
    RecordingListResponse,
    RoomConfig,
    RoomCreateDetailsResponse,
    RoomDetailsResponse,
    RoomsListingResponse,
    RoomType,
    StreamerToken,
    SubscribeMode,
    SubscribeTracksBody,
    TrackForwarding,
    VideoCodec,
    ViewerToken,
    WebRTCMetadata,
)
from fishjam._openapi_client.types import UNSET, Unset
from fishjam.agent import Agent
from fishjam.api._client import Client
from fishjam.errors import (
    InvalidFishjamCredentialsError,
)
from fishjam.utils import get_livestream_whep_url, get_livestream_whip_url


@dataclass
class Room:
    """Description of the room state.

    Attributes:
        config: Room configuration.
        id: Room ID.
        peers: List of all peers.
        composition_info: The composition the room's tracks are forwarded into,
            when `FishjamClient.forward_room_tracks` has linked one.
    """

    config: RoomConfig
    """Room configuration"""
    id: str
    """Room ID"""
    peers: list[Peer]
    """List of all peers"""
    composition_info: CompositionInfo | None = None
    """The composition the room's tracks are forwarded into"""


@dataclass
class RoomOptions:
    """Description of a room options.

    Attributes:
        max_peers: Maximum amount of peers allowed into the room.
        video_codec: Enforces video codec for each peer in the room.
        webhook_url: URL where Fishjam notifications will be sent.
        room_type: The use-case of the room. If not provided, this defaults
            to conference.
        public: True if livestream viewers can omit specifying a token.
        batch_webhook_notifications: If true, webhook notifications for this room
            are coalesced into a single NotificationBatch per HTTP send instead
            of one request per notification.
    """

    max_peers: int | None = None
    """Maximum amount of peers allowed into the room"""
    video_codec: Literal["h264", "vp8"] | None = None
    """Enforces video codec for each peer in the room"""
    webhook_url: str | None = None
    """URL where Fishjam notifications will be sent"""
    room_type: Literal[
        "conference",
        "audio_only",
        "livestream",
        "full_feature",
        "broadcaster",
        "audio_only_livestream",
    ] = "conference"
    """The use-case of the room. If not provided, this defaults to conference."""
    public: bool = False
    """True if livestream viewers can omit specifying a token."""
    batch_webhook_notifications: bool = False
    """Coalesce webhook notifications into a single NotificationBatch per send."""


@dataclass
class PeerOptions:
    """Options specific to a WebRTC Peer.

    Attributes:
        metadata: Peer metadata.
        subscribe_mode: Configuration of peer's subscribing policy.
    """

    metadata: dict[str, Any] | None = None
    """Peer metadata"""
    subscribe_mode: Literal["auto", "manual"] = "auto"
    """Configuration of peer's subscribing policy"""


@dataclass
class AgentOutputOptions:
    """Options of the desired format of audio tracks going from Fishjam to the agent.

    Attributes:
        audio_format: The format of the audio stream (e.g., 'pcm16').
        audio_sample_rate: The sample rate of the audio stream.
    """

    audio_format: Literal["pcm16"] = "pcm16"
    audio_sample_rate: Literal[16000, 24000] = 16000


@dataclass
class AgentOptions:
    """Options specific to an Agent Peer.

    Attributes:
        output: Configuration for the agent's output options.
        subscribe_mode: Configuration of peer's subscribing policy.
    """

    output: AgentOutputOptions = field(default_factory=AgentOutputOptions)

    subscribe_mode: Literal["auto", "manual"] = "auto"


class FishjamClient(Client):
    """Allows for managing rooms."""

    def __init__(
        self,
        fishjam_id: str,
        management_token: str,
    ):
        """Create a FishjamClient instance.

        Does not contact the Fishjam backend — use :meth:`create_and_verify`
        or :meth:`check_credentials` to verify credentials live.

        Args:
            fishjam_id: The unique identifier for the Fishjam instance.
            management_token: The token used for authenticating management operations.
        """
        super().__init__(fishjam_id=fishjam_id, management_token=management_token)

    @classmethod
    def create_and_verify(
        cls, *, fishjam_id: str, management_token: str
    ) -> "FishjamClient":
        """Construct a FishjamClient and verify its credentials against the backend.

        Args:
            fishjam_id: The unique identifier for the Fishjam instance.
            management_token: The token used for authenticating management operations.

        Returns:
            FishjamClient: A client whose credentials have been verified.

        Raises:
            InvalidFishjamCredentialsError: If the token is rejected.
        """
        client = cls(fishjam_id=fishjam_id, management_token=management_token)
        client.check_credentials()
        return client

    def check_credentials(self) -> None:
        """Verify the management token via a single ``/validate`` call.

        Raises:
            InvalidFishjamCredentialsError: If the token is rejected.
        """
        response = credentials_validate_credentials.sync_detailed(client=self.client)
        self._handle_deprecation_header(response.headers)

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise InvalidFishjamCredentialsError("Invalid Fishjam credentials")

    def create_peer(
        self,
        room_id: str,
        options: PeerOptions | None = None,
    ) -> tuple[Peer, str]:
        """Creates a peer in the room.

        Args:
            room_id: The ID of the room where the peer will be created.
            options: Configuration options for the peer. Defaults to None.

        Returns:
            A tuple containing:
                - Peer: The created peer object.
                - str: The peer token needed to authenticate to Fishjam.
        """
        options = options or PeerOptions()

        peer_metadata = self.__parse_peer_metadata(options.metadata)
        peer_options = PeerOptionsWebRTC(
            metadata=peer_metadata,
            subscribe_mode=SubscribeMode(options.subscribe_mode),
        )
        body = PeerConfigWebRTC(type_=PeerConfigWebRTCType.WEBRTC, options=peer_options)

        resp = cast(
            PeerDetailsResponse,
            self._request(room_add_peer, room_id=room_id, body=body),
        )

        return (resp.data.peer, resp.data.token)

    def create_agent(self, room_id: str, options: AgentOptions | None = None):
        """Creates an agent in the room.

        Args:
            room_id: The ID of the room where the agent will be created.
            options: Configuration options for the agent. Defaults to None.

        Returns:
            Agent: The created agent instance initialized with peer ID, room ID, token,
                and Fishjam URL.
        """
        options = options or AgentOptions()
        body = PeerConfigAgent(
            type_=PeerConfigAgentType.AGENT,
            options=PeerOptionsAgent(
                output=AgentOutput(
                    audio_format=AudioFormat(options.output.audio_format),
                    audio_sample_rate=AudioSampleRate(options.output.audio_sample_rate),
                ),
                subscribe_mode=SubscribeMode(options.subscribe_mode),
            ),
        )

        resp = cast(
            PeerDetailsResponse,
            self._request(room_add_peer, room_id=room_id, body=body),
        )

        socket_base_url = self._peer_socket_base_url(resp.data.peer_websocket_url)
        return Agent(resp.data.peer.id, room_id, resp.data.token, socket_base_url)

    def _peer_socket_base_url(self, peer_websocket_url: str | Unset) -> str:
        if isinstance(peer_websocket_url, Unset) or not peer_websocket_url:
            return self._fishjam_url

        url = peer_websocket_url
        if "://" not in url:
            url = f"https://{url}"
        for suffix in ("/socket/peer/websocket", "/socket/agent/websocket"):
            url = url.removesuffix(suffix)
        return url

    def create_vapi_agent(
        self,
        room_id: str,
        options: PeerOptionsVapi,
    ) -> Peer:
        """Creates a vapi agent in the room.

        Args:
            room_id: The ID of the room where the vapi agent will be created.
            options: Configuration options for the vapi peer.

        Returns:
            - Peer: The created peer object.
        """
        body = PeerConfigVAPI(type_=PeerConfigVAPIType.VAPI, options=options)

        resp = cast(
            PeerDetailsResponse,
            self._request(room_add_peer, room_id=room_id, body=body),
        )

        return resp.data.peer

    def create_room(self, options: RoomOptions | None = None) -> Room:
        """Creates a new room.

        Args:
            options: Configuration options for the room. Defaults to None.

        Returns:
            Room: The created Room object.
        """
        options = options or RoomOptions()

        if options.video_codec is None:
            codec = UNSET
        else:
            codec = VideoCodec(options.video_codec)

        config = RoomConfig(
            max_peers=options.max_peers,
            video_codec=codec,
            webhook_url=options.webhook_url,
            room_type=RoomType(options.room_type),
            public=options.public,
            batch_webhook_notifications=options.batch_webhook_notifications,
        )

        room = cast(
            RoomCreateDetailsResponse, self._request(room_create_room, body=config)
        ).data.room

        return _to_room(room)

    def get_all_rooms(self) -> list[Room]:
        """Returns list of all rooms.

        Returns:
            list[Room]: A list of all available Room objects.
        """
        rooms = cast(RoomsListingResponse, self._request(room_get_all_rooms)).data

        return [_to_room(room) for room in rooms]

    def get_room(self, room_id: str) -> Room:
        """Returns room with the given id.

        Args:
            room_id: The ID of the room to retrieve.

        Returns:
            Room: The Room object corresponding to the given ID.
        """
        room = cast(
            RoomDetailsResponse, self._request(room_get_room, room_id=room_id)
        ).data

        return _to_room(room)

    def delete_peer(self, room_id: str, peer_id: str) -> None:
        """Deletes a peer from a room.

        Args:
            room_id: The ID of the room the peer belongs to.
            peer_id: The ID of the peer to delete.
        """
        return self._request(room_delete_peer, id=peer_id, room_id=room_id)

    def delete_room(self, room_id: str) -> None:
        """Deletes a room.

        Args:
            room_id: The ID of the room to delete.
        """
        return self._request(room_delete_room, room_id=room_id)

    def refresh_peer_token(self, room_id: str, peer_id: str) -> str:
        """Refreshes a peer token.

        Args:
            room_id: The ID of the room.
            peer_id: The ID of the peer whose token needs refreshing.

        Returns:
            str: The new peer token.
        """
        response = cast(
            PeerRefreshTokenResponse,
            self._request(room_refresh_token, id=peer_id, room_id=room_id),
        )

        return response.data.token

    def forward_room_tracks(self, room_id: str, composition_url: str) -> None:
        """Forwards every track published in the room into a composition.

        The composition composes them into its outputs. Pass the composition's
        address, as returned by
        `fishjam.CompositionClient.composition_url`.

        Args:
            room_id: The ID of the room to forward tracks from.
            composition_url: The address of the composition to forward tracks to.
        """
        self._request(
            track_forwardings_create,
            room_id=room_id,
            body=TrackForwarding(composition_url=composition_url),
        )

    def livestream_whip_url(self) -> str:
        """Where to publish a livestream.

        Pair it with a token from
        `fishjam.FishjamClient.create_livestream_streamer_token`. A composition
        reaches viewers by sending a WHIP output here.

        Returns:
            str: The address a WHIP publisher sends the livestream to.
        """
        return get_livestream_whip_url(self._fishjam_id)

    def livestream_whep_url(self) -> str:
        """Where to watch a livestream.

        Pair it with a token from
        `fishjam.FishjamClient.create_livestream_viewer_token`, sent as a bearer
        token by the WHEP player.

        Returns:
            str: The address a WHEP viewer plays the livestream from.
        """
        return get_livestream_whep_url(self._fishjam_id)

    def create_livestream_viewer_token(self, room_id: str) -> str:
        """Generates a viewer token for livestream rooms.

        Args:
            room_id: The ID of the livestream room.

        Returns:
            str: The generated viewer token.
        """
        response = cast(
            ViewerToken, self._request(viewer_generate_viewer_token, room_id=room_id)
        )

        return response.token

    def create_livestream_streamer_token(self, room_id: str) -> str:
        """Generates a streamer token for livestream rooms.

        Args:
            room_id: The ID of the livestream room.

        Returns:
            str: The generated streamer token.
        """
        response = cast(
            StreamerToken,
            self._request(streamer_generate_streamer_token, room_id=room_id),
        )

        return response.token

    def create_moq_access(
        self,
        publish_path: str | None = None,
        subscribe_path: str | None = None,
    ) -> MoqAccess:
        """Generates MoQ relay connection details.

        Args:
            publish_path: Path the access grants publish access to.
            subscribe_path: Path the access grants subscribe access to.

        Returns:
            MoqAccess: The relay connection details, containing the
            ``connection_url`` (with the JWT embedded as a ``?jwt=`` query
            parameter) and the ``token`` itself.
        """
        config = MoqAccessConfig(
            publish_path=publish_path, subscribe_path=subscribe_path
        )
        response = cast(
            MoqAccess,
            self._request(moq_create_access, body=config),
        )

        return response

    def create_recording(
        self,
        source: CompositionSource,
        metadata: dict[str, Any] | None = None,
    ) -> Recording:
        """Creates a new recording.

        Capturing starts synchronously, so the returned recording is `active`.

        Args:
            source: The source of the recording.
            metadata: Free-form metadata used to organize and filter recordings.

        Returns:
            Recording: The created recording.
        """
        if metadata is None:
            config_metadata = UNSET
        else:
            config_metadata = RecordingConfigMetadataType0()
            for key, value in metadata.items():
                config_metadata.additional_properties[key] = value

        config = RecordingConfig(source=source, metadata=config_metadata)

        resp = cast(
            RecordingDetailsResponse,
            self._request(recording_create_recording, body=config),
        )

        return resp.data

    def get_recording(self, recording_id: str) -> Recording:
        """Returns the recording with the given id.

        Args:
            recording_id: The ID of the recording to retrieve.

        Returns:
            Recording: The recording corresponding to the given ID.
        """
        resp = cast(
            RecordingDetailsResponse,
            self._request(recording_get_recording, recording_id=recording_id),
        )

        return resp.data

    def get_all_recordings(
        self, metadata: dict[str, Any] | None = None
    ) -> list[Recording]:
        """Returns a list of all recordings, optionally filtered by metadata.

        Args:
            metadata: If given, only recordings whose metadata contains all
                the given key-value pairs are returned. Nested dicts match
                nested metadata keys.

        Returns:
            list[Recording]: A list of all matching recordings.
        """
        # the API expects the deepObject query format
        # (`metadata[key]=value`, `metadata[key][nested]=value`), but the
        # generated client serializes the filter keys at the top level, so
        # prefix and flatten them here
        if metadata is None:
            metadata_query = UNSET
        else:
            metadata_query = ListRecordingsMetadata()
            self.__flatten_metadata_filter(
                "metadata", metadata, metadata_query.additional_properties
            )

        resp = cast(
            RecordingListResponse,
            self._request(recording_list_recordings, metadata=metadata_query),
        )

        return resp.data

    def stop_recording(self, recording_id: str) -> Recording:
        """Stops an active recording.

        Finalization is asynchronous: the recording stays `active` until the
        capture is finalized, then becomes `finished`. Stopping a recording
        that is no longer active is a no-op.

        Args:
            recording_id: The ID of the recording to stop.

        Returns:
            Recording: The stopped recording.
        """
        resp = cast(
            RecordingDetailsResponse,
            self._request(recording_stop_recording, recording_id=recording_id),
        )

        return resp.data

    def delete_recording(self, recording_id: str) -> None:
        """Deletes a recording. Its stored media is removed asynchronously.

        A recording that is still `active` cannot be deleted — stop it first
        or wait for it to finish.

        Args:
            recording_id: The ID of the recording to delete.
        """
        self._request(recording_delete_recording, recording_id=recording_id)

    def subscribe_peer(self, room_id: str, peer_id: str, target_peer_id: str):
        """Subscribes a peer to all tracks of another peer.

        Args:
            room_id: The ID of the room.
            peer_id: The ID of the subscribing peer.
            target_peer_id: The ID of the peer to subscribe to.
        """
        self._request(
            room_subscribe_peer,
            room_id=room_id,
            id=peer_id,
            peer_id=target_peer_id,
        )

    def subscribe_tracks(self, room_id: str, peer_id: str, track_ids: list[str]):
        """Subscribes a peer to specific tracks of another peer.

        Args:
            room_id: The ID of the room.
            peer_id: The ID of the subscribing peer.
            track_ids: A list of track IDs to subscribe to.
        """
        self._request(
            room_subscribe_tracks,
            room_id=room_id,
            id=peer_id,
            body=SubscribeTracksBody(track_ids=track_ids),
        )

    def __flatten_metadata_filter(
        self, prefix: str, metadata: dict[str, Any], params: dict[str, Any]
    ) -> None:
        for key, value in metadata.items():
            param_key = f"{prefix}[{key}]"
            if isinstance(value, dict):
                self.__flatten_metadata_filter(param_key, value, params)
            elif value is None:
                # the generated client drops `None` params; the API compares
                # values as JSON strings, so send the JSON representation
                params[param_key] = "null"
            else:
                params[param_key] = value

    def __parse_peer_metadata(self, metadata: dict | None) -> WebRTCMetadata:
        peer_metadata = WebRTCMetadata()

        if not metadata:
            return peer_metadata

        for key, value in metadata.items():
            peer_metadata.additional_properties[key] = value

        return peer_metadata


def _to_room(room) -> Room:
    composition_info = room.composition_info

    return Room(
        config=room.config,
        id=room.id,
        peers=room.peers,
        composition_info=None
        if isinstance(composition_info, Unset)
        else composition_info,
    )
