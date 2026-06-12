""".. include:: ../README.md"""

# pylint: disable=locally-disabled, no-name-in-module, import-error

# Exceptions and Server Messages

# API
# pylint: disable=locally-disabled, no-name-in-module, import-error

# Exceptions and Server Messages
from fishjam import agent, errors, events, integrations, peer, room, version
from fishjam._openapi_client.models import PeerMetadata

# API
from fishjam._webhook_notifier import decode_server_notifications, receive_binary
from fishjam._ws_notifier import FishjamNotifier
from fishjam.api._fishjam_client import (
    AgentOptions,
    AgentOutputOptions,
    FishjamClient,
    Peer,
    PeerOptions,
    PeerOptionsVapi,
    Room,
    RoomOptions,
)
from fishjam.errors import InvalidFishjamCredentialsError, MissingFishjamIdError

__version__ = version.__version__

__all__ = [
    "FishjamClient",
    "FishjamNotifier",
    "decode_server_notifications",
    "receive_binary",
    "PeerMetadata",
    "PeerOptions",
    "PeerOptionsVapi",
    "RoomOptions",
    "AgentOptions",
    "AgentOutputOptions",
    "Room",
    "Peer",
    "MissingFishjamIdError",
    "InvalidFishjamCredentialsError",
    "events",
    "errors",
    "room",
    "peer",
    "agent",
    "integrations",
]


__docformat__ = "restructuredtext"
