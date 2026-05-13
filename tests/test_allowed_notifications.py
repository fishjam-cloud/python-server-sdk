import dataclasses

from fishjam import events
from fishjam.events import _protos
from fishjam.events._protos.fishjam import ServerMessage
from fishjam.events.allowed_notifications import ALLOWED_NOTIFICATIONS

# Types intentionally NOT published as SDK notifications.
# Adding a new oneof member to ServerMessage.content forces a maintainer
# decision: either add it to ALLOWED_NOTIFICATIONS (and re-export from
# fishjam.events), or add it here with a comment.
IGNORED_NOTIFICATIONS = {
    # Auth / subscribe handshake — transport-level, not user-facing events.
    "ServerMessageAuthenticated",
    "ServerMessageAuthRequest",
    "ServerMessageSubscribeRequest",
    "ServerMessageSubscribeResponse",
    # Not surfaced to SDK users - support for compositions is REST api only
    # and not supported in SDKs
    "ServerMessageTrackForwarding",
    "ServerMessageTrackForwardingRemoved",
    "ServerMessageVadNotification",
    # Webhook-only transport wrapper; the WebSocket notifier never receives it.
    "ServerMessageNotificationBatch",
    # Deprecated in the proto.
    "ServerMessageStreamConnected",
    "ServerMessageStreamDisconnected",
    "ServerMessageHlsPlayable",
    "ServerMessageHlsUploaded",
    "ServerMessageHlsUploadCrashed",
    "ServerMessageComponentCrashed",
}


def _oneof_content_types() -> list[type]:
    types = []
    for field in dataclasses.fields(ServerMessage):
        meta = field.metadata.get("betterproto")
        if meta is not None and getattr(meta, "group", None) == "content":
            types.append(getattr(_protos.fishjam, field.type))
    return types


def test_every_content_oneof_is_allowed_or_explicitly_ignored():
    allowed_names = {cls.__name__ for cls in ALLOWED_NOTIFICATIONS}
    undecided = [
        cls.__name__
        for cls in _oneof_content_types()
        if cls.__name__ not in allowed_names
        and cls.__name__ not in IGNORED_NOTIFICATIONS
    ]
    assert not undecided, (
        "New ServerMessage.content oneof members found without a maintainer "
        "decision. Add each to ALLOWED_NOTIFICATIONS (and re-export from "
        "fishjam.events) or to IGNORED_NOTIFICATIONS in this test:\n  - "
        + "\n  - ".join(sorted(undecided))
    )


def test_allowed_and_ignored_are_disjoint():
    overlap = {cls.__name__ for cls in ALLOWED_NOTIFICATIONS} & IGNORED_NOTIFICATIONS
    assert not overlap, f"Types cannot be both allowed and ignored: {overlap}"


def test_allowed_notifications_are_reexported_from_package():
    missing = [
        cls.__name__
        for cls in ALLOWED_NOTIFICATIONS
        if cls.__name__ not in events.__all__ or not hasattr(events, cls.__name__)
    ]
    assert not missing, (
        "Every ALLOWED_NOTIFICATIONS type must be re-exported from "
        f"fishjam.events. Missing: {missing}"
    )
