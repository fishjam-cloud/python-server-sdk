"""
.. include:: ../../docs/server_notifications.md
"""

# Exported messages
from fishjam.events._protos.fishjam import (
    ServerMessagePeerAdded,
    ServerMessagePeerConnected,
    ServerMessagePeerCrashed,
    ServerMessagePeerDeleted,
    ServerMessagePeerDisconnected,
    ServerMessagePeerMetadataUpdated,
    ServerMessageRoomCrashed,
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
    ServerMessageStreamConnected,
    ServerMessageStreamDisconnected,
    ServerMessageTrack,
    ServerMessageTrackAdded,
    ServerMessageTrackData,
    ServerMessageTrackMetadataUpdated,
    ServerMessageTrackRemoved,
    ServerMessageTrackType,
    ServerMessageViewerConnected,
    ServerMessageViewerDisconnected,
)

__all__ = [
    "ServerMessageRoomCreated",
    "ServerMessageRoomDeleted",
    "ServerMessageRoomCrashed",
    "ServerMessagePeerAdded",
    "ServerMessagePeerConnected",
    "ServerMessagePeerDeleted",
    "ServerMessagePeerDisconnected",
    "ServerMessagePeerMetadataUpdated",
    "ServerMessagePeerCrashed",
    "ServerMessageStreamConnected",
    "ServerMessageStreamDisconnected",
    "ServerMessageTrack",
    "ServerMessageTrackType",
    "ServerMessageTrackAdded",
    "ServerMessageTrackData",
    "ServerMessageTrackMetadataUpdated",
    "ServerMessageTrackRemoved",
    "ServerMessageViewerConnected",
    "ServerMessageViewerDisconnected",
]
