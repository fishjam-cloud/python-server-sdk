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
from fishjam._openapi_client.api.viewers import (
    generate_viewer_token as viewer_generate_viewer_token,
)
from fishjam._openapi_client.models import (
    AgentOutput,
    AudioFormat,
    AudioSampleRate,
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
    RoomConfig,
    RoomCreateDetailsResponse,
    RoomDetailsResponse,
    RoomsListingResponse,
    RoomType,
    StreamerToken,
    SubscribeMode,
    SubscribeTracksBody,
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


@dataclass
class Room:
    """Description of the room state.

    Attributes:
        config: Room configuration.
        id: Room ID.
        peers: List of all peers.
    """

    config: RoomConfig
    """Room configuration"""
    id: str
    """Room ID"""
    peers: list[Peer]
    """List of all peers"""


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
        # Fishjam deployments with a separate media node return the websocket
        # address the peer must connect to; older deployments omit it, in which
        # case the socket lives on the Fishjam URL itself.
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

        return Room(config=room.config, id=room.id, peers=room.peers)

    def get_all_rooms(self) -> list[Room]:
        """Returns list of all rooms.

        Returns:
            list[Room]: A list of all available Room objects.
        """
        rooms = cast(RoomsListingResponse, self._request(room_get_all_rooms)).data

        return [
            Room(config=room.config, id=room.id, peers=room.peers) for room in rooms
        ]

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

        return Room(config=room.config, id=room.id, peers=room.peers)

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

    def __parse_peer_metadata(self, metadata: dict | None) -> WebRTCMetadata:
        peer_metadata = WebRTCMetadata()

        if not metadata:
            return peer_metadata

        for key, value in metadata.items():
            peer_metadata.additional_properties[key] = value

        return peer_metadata
