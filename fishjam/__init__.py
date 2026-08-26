""".. include:: ../README.md"""

# pylint: disable=locally-disabled, no-name-in-module, import-error

# Exceptions and Server Messages

# API
# pylint: disable=locally-disabled, no-name-in-module, import-error

# Exceptions and Server Messages
from fishjam import (
    agent,
    composition,
    errors,
    events,
    integrations,
    peer,
    recording,
    room,
    version,
)
from fishjam._openapi_client.models import PeerMetadata

# API
from fishjam._webhook_notifier import (
    decode_server_notifications,
    receive_binary,
    verify_webhook_signature,
)
from fishjam._ws_notifier import FishjamNotifier
from fishjam.api._composition_client import (
    CompositionClient,
    Mp4InputDurations,
    WhipInputTarget,
)
from fishjam.api._fishjam_client import (
    AgentOptions,
    AgentOutputOptions,
    FishjamClient,
    MoqAccess,
    Peer,
    PeerOptions,
    PeerOptionsVapi,
    Recording,
    Room,
    RoomOptions,
)
from fishjam.errors import (
    InvalidFishjamCredentialsError,
    MissingFishjamIdError,
    StaleSdkError,
)

__version__ = version.__version__

__all__ = [
    "FishjamClient",
    "CompositionClient",
    "WhipInputTarget",
    "Mp4InputDurations",
    "FishjamNotifier",
    "decode_server_notifications",
    "receive_binary",
    "verify_webhook_signature",
    "PeerMetadata",
    "PeerOptions",
    "PeerOptionsVapi",
    "RoomOptions",
    "AgentOptions",
    "AgentOutputOptions",
    "Room",
    "Peer",
    "Recording",
    "MoqAccess",
    "MissingFishjamIdError",
    "InvalidFishjamCredentialsError",
    "StaleSdkError",
    "events",
    "errors",
    "room",
    "peer",
    "recording",
    "agent",
    "integrations",
    "composition",
]


__docformat__ = "restructuredtext"
