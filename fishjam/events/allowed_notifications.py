from typing import Union

from fishjam.errors import StaleSdkError
from fishjam.events import (
    ServerMessageChannelAdded,
    ServerMessageChannelRemoved,
    ServerMessagePeerAdded,
    ServerMessagePeerConnected,
    ServerMessagePeerCrashed,
    ServerMessagePeerDeleted,
    ServerMessagePeerDisconnected,
    ServerMessagePeerMetadataUpdated,
    ServerMessageRecordingStatusChanged,
    ServerMessageRecordingStatusChangedStatus,
    ServerMessageRoomCrashed,
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
    ServerMessageStreamerConnected,
    ServerMessageStreamerDisconnected,
    ServerMessageTrackAdded,
    ServerMessageTrackMetadataUpdated,
    ServerMessageTrackRemoved,
    ServerMessageViewerConnected,
    ServerMessageViewerDisconnected,
)

ALLOWED_NOTIFICATIONS = (
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
    ServerMessageRoomCrashed,
    ServerMessagePeerAdded,
    ServerMessagePeerDeleted,
    ServerMessagePeerConnected,
    ServerMessagePeerDisconnected,
    ServerMessagePeerMetadataUpdated,
    ServerMessagePeerCrashed,
    ServerMessageStreamerConnected,
    ServerMessageStreamerDisconnected,
    ServerMessageChannelAdded,
    ServerMessageChannelRemoved,
    ServerMessageViewerConnected,
    ServerMessageViewerDisconnected,
    ServerMessageTrackAdded,
    ServerMessageTrackRemoved,
    ServerMessageTrackMetadataUpdated,
    ServerMessageRecordingStatusChanged,
)

AllowedNotification = Union[
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
    ServerMessageRoomCrashed,
    ServerMessagePeerAdded,
    ServerMessagePeerDeleted,
    ServerMessagePeerConnected,
    ServerMessagePeerDisconnected,
    ServerMessagePeerMetadataUpdated,
    ServerMessagePeerCrashed,
    ServerMessageStreamerConnected,
    ServerMessageStreamerDisconnected,
    ServerMessageChannelAdded,
    ServerMessageChannelRemoved,
    ServerMessageViewerConnected,
    ServerMessageViewerDisconnected,
    ServerMessageTrackAdded,
    ServerMessageTrackRemoved,
    ServerMessageTrackMetadataUpdated,
    ServerMessageRecordingStatusChanged,
]


# Raises instead of falling back: STATUS_UNSPECIFIED or an unknown wire value
# both mean this SDK is likely too old to parse the statuses the server sends.
def validate_notification(notification: AllowedNotification) -> None:
    if isinstance(notification, ServerMessageRecordingStatusChanged):
        try:
            status = ServerMessageRecordingStatusChangedStatus(notification.status)
        except ValueError:
            raise StaleSdkError(notification.status) from None
        if status == ServerMessageRecordingStatusChangedStatus.STATUS_UNSPECIFIED:
            raise StaleSdkError(status)
