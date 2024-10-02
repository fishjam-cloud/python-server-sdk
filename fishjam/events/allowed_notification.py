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
