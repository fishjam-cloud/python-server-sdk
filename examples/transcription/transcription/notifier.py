from fishjam import FishjamNotifier
from fishjam.events import (
    ServerMessagePeerConnected,
    ServerMessagePeerDisconnected,
    ServerMessagePeerType,
)
from fishjam.events.allowed_notifications import AllowedNotification

from .config import FISHJAM_ID, FISHJAM_TOKEN
from .room import RoomService


def make_notifier(room_service: RoomService):
    notifier = FishjamNotifier(
        FISHJAM_ID,
        FISHJAM_TOKEN,
    )

    @notifier.on_server_notification
    def _(notification: AllowedNotification):
        match notification:
            case ServerMessagePeerConnected(
                peer_id=peer_id,
                room_id=room_id,
                peer_type=ServerMessagePeerType.PEER_TYPE_WEBRTC,
            ):
                handle_peer_connected(peer_id, room_id)

            case ServerMessagePeerDisconnected(
                peer_id=peer_id,
                room_id=room_id,
                peer_type=ServerMessagePeerType.PEER_TYPE_WEBRTC,
            ):
                handle_peer_disconnected(peer_id, room_id)

    def handle_peer_connected(peer_id: str, room_id: str):
        if room_id == room_service.room.id:
            room_service.agent.on_peer_enter(peer_id)

    def handle_peer_disconnected(peer_id: str, room_id: str):
        if room_id == room_service.room.id:
            room_service.agent.on_peer_leave(peer_id)

    return notifier
