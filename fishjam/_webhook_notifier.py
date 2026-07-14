"""Module for decoding received webhook notifications from Fishjam."""

import hmac
import warnings
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


def decode_server_notifications(binary: bytes) -> List[AllowedNotification]:
    """Decode a received protobuf payload into a list of notifications.

    Handles both single notifications and batches transparently: a single
    notification is returned as a one-element list, a batch is unpacked into
    its members (in order), and anything unsupported yields an empty list.

    The available notifications are listed in the `fishjam.events` module.

    Args:
        binary: The raw binary data received from the webhook.

    Returns:
        list[AllowedNotification]: The decoded notifications, in order. Empty
            when the payload carries no supported notification.
    """
    message = ServerMessage().parse(binary)
    _which, content = betterproto.which_one_of(message, "content")

    if isinstance(content, ServerMessageNotificationBatch):
        return _unpack_batch(content)

    if isinstance(content, ALLOWED_NOTIFICATIONS):
        return [content]

    return []


def verify_webhook_signature(body: bytes, signature: str, secret: str) -> bool:
    """Verify the `x-fishjam-signature-256` header of a raw webhook body.

    Accepts the `sha256=<hex>` format sent by Fishjam (the prefix is
    optional) and compares in constant time. Call this with the raw request
    body before passing it to `decode_server_notifications`.

    Args:
        body: The raw binary body of the webhook request.
        signature: The value of the `x-fishjam-signature-256` header.
        secret: The webhook secret configured in Fishjam.

    Returns:
        bool: True when the signature matches the body, False otherwise.
    """
    expected = hmac.new(secret.encode(), body, "sha256").hexdigest()
    provided = signature.strip().removeprefix("sha256=")
    return hmac.compare_digest(provided, expected)


def receive_binary(
    binary: bytes,
) -> Union[AllowedNotification, List[AllowedNotification], None]:
    """Transforms a received protobuf notification into a notification instance.

    .. deprecated::
        Use `decode_server_notifications` instead, which always returns a list
        and handles batched payloads with a single, consistent return type.

    The available notifications are listed in `fishjam.events` module.

    Args:
        binary: The raw binary data received from the webhook.

    Returns:
        AllowedNotification: A single notification when the payload carries one.
        list[AllowedNotification]: The unpacked notifications, in order, when the
            payload is a batch (webhook batching enabled).
        None: When the payload is not a supported notification.
    """
    warnings.warn(
        "receive_binary is deprecated; use decode_server_notifications instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    message = ServerMessage().parse(binary)
    _which, content = betterproto.which_one_of(message, "content")

    if isinstance(content, ServerMessageNotificationBatch):
        return _unpack_batch(content)

    if isinstance(content, ALLOWED_NOTIFICATIONS):
        return content

    return None
