"""Module for decoding received webhook notifications from Fishjam."""

from typing import List, Union

import betterproto

from fishjam.events._protos.fishjam import (
    ServerMessage,
    ServerMessageNotificationBatch,
)
from fishjam.events.allowed_notifications import (
    ALLOWED_NOTIFICATIONS,
    AllowedNotification,
)


def _content_of(message: ServerMessage) -> Union[AllowedNotification, None]:
    """Return the message's `content` oneof if it is a supported notification."""
    _which, content = betterproto.which_one_of(message, "content")
    if isinstance(content, ALLOWED_NOTIFICATIONS):
        return content
    return None


def _unpack_batch(
    batch: ServerMessageNotificationBatch,
) -> List[AllowedNotification]:
    """Flatten a notification batch into its supported notifications, in order.

    Members whose content is not a supported notification are skipped.

    Returns:
        list[AllowedNotification]: The supported notifications from the batch.
    """
    notifications = []
    for message in batch.notifications:
        notification = _content_of(message)
        if notification is not None:
            notifications.append(notification)
    return notifications


def receive_binary(
    binary: bytes,
) -> Union[AllowedNotification, List[AllowedNotification], None]:
    """Transforms a received protobuf notification into a notification instance.

    The available notifications are listed in `fishjam.events` module.

    Args:
        binary: The raw binary data received from the webhook.

    Returns:
        AllowedNotification: A single notification when the payload carries one.
        list[AllowedNotification]: The unpacked notifications, in order, when the
            payload is a batch (webhook batching enabled).
        None: When the payload is not a supported notification.
    """
    message = ServerMessage().parse(binary)
    _which, content = betterproto.which_one_of(message, "content")

    if isinstance(content, ServerMessageNotificationBatch):
        return _unpack_batch(content)

    if isinstance(content, ALLOWED_NOTIFICATIONS):
        return content

    return None
