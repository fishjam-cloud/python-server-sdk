"""
Module defining a function allowing decoding received webhook 
notification from fishjam to notification structs.
"""

from typing import Union

import betterproto

from fishjam.events import (
    ServerMessagePeerAdded,
    ServerMessagePeerConnected,
    ServerMessagePeerCrashed,
    ServerMessagePeerDeleted,
    ServerMessagePeerDisconnected,
    ServerMessagePeerMetadataUpdated,
    ServerMessageRoomCrashed,
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
    ServerMessageTrackAdded,
    ServerMessageTrackMetadataUpdated,
    ServerMessageTrackRemoved,
)
from fishjam.events._protos.fishjam import ServerMessage

ALLOWED_NOTIFICATION = (
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
    ServerMessageRoomCrashed,
    ServerMessagePeerAdded,
    ServerMessagePeerDeleted,
    ServerMessagePeerConnected,
    ServerMessagePeerDisconnected,
    ServerMessagePeerMetadataUpdated,
    ServerMessagePeerCrashed,
    ServerMessageTrackAdded,
    ServerMessageTrackRemoved,
    ServerMessageTrackMetadataUpdated,
)


def receive_binary(binary: bytes) -> Union[betterproto.Message, None]:
    """
    Transform received protobuf notification to adequate notification instance.
    The available notifications are listed in `fishjam.events` module.
    """
    message = ServerMessage().parse(binary)
    _which, message = betterproto.which_one_of(message, "content")

    if isinstance(message, ALLOWED_NOTIFICATION):
        return message

    return None
