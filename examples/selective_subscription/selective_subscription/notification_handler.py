from typing import Dict, Set
import asyncio

from .config import FISHJAM_ID, FISHJAM_TOKEN, FISHJAM_URL
from .room_service import RoomService
from fishjam._ws_notifier import FishjamNotifier
from fishjam.events import (
    ServerMessagePeerType,
    ServerMessagePeerConnected,
    ServerMessagePeerDisconnected,
    ServerMessageTrackAdded,
    ServerMessageTrackRemoved,
)
from fishjam.events.allowed_notifications import AllowedNotification


class NotificationHandler:
    """Handles Fishjam server notifications for selective subscription.
    """
    
    def __init__(self, room_service: RoomService):
        self.room_service = room_service
        self._notifier = FishjamNotifier(FISHJAM_ID, FISHJAM_TOKEN)
        @self._notifier.on_server_notification
        async def _(notification: AllowedNotification):
            match notification:
                case ServerMessagePeerConnected(
                    peer_type=ServerMessagePeerType.PEER_TYPE_WEBRTC,
                ):
                    await handle_peer_connected(notification)
                case ServerMessagePeerDisconnected(
                    peer_type=ServerMessagePeerType.PEER_TYPE_WEBRTC,
                ):
                    await handle_peer_disconnected(notification)
                case ServerMessageTrackAdded(
                    peer_type=ServerMessagePeerType.PEER_TYPE_WEBRTC,
                ):
                    await handle_track_added(notification)
                case ServerMessageTrackRemoved(
                    peer_type=ServerMessagePeerType.PEER_TYPE_WEBRTC,
                ):
                    await handle_track_removed(notification)

        async def handle_peer_connected(notification: ServerMessagePeerConnected):
            print(f"Peer connected: {notification.peer_id}")

        async def handle_peer_disconnected(notification: ServerMessagePeerDisconnected):
            print(f"Peer disconnected: {notification.peer_id}")

        async def handle_track_added(notification: ServerMessageTrackAdded):
            print(f"Track added: {notification.track}")

        async def handle_track_removed(notification: ServerMessageTrackRemoved):
            print(f"Track removed: {notification.track}")
    
    async def start(self) -> None:
        """Long-running coroutine that connects the notifier and processes messages."""
        await self._notifier.connect()
            

