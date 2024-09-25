"""
    .. include:: ../README.md
"""

# pylint: disable=locally-disabled, no-name-in-module, import-error

# Exceptions and Server Messages

# API
# pylint: disable=locally-disabled, no-name-in-module, import-error

# Exceptions and Server Messages
from fishjam import errors, events

# API
from fishjam._webhook_notifier import receive_binary
from fishjam._ws_notifier import Notifier
from fishjam.api._room_api import PeerOptions, RoomApi, RoomOptions

__all__ = [
    "RoomApi",
    "Notifier",
    "receive_binary",
    "PeerOptions",
    "RoomOptions",
    "events",
    "errors",
]

__docformat__ = "restructuredtext"
