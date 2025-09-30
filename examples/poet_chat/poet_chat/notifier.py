from agents.realtime import RealtimeSession

from fishjam import FishjamNotifier
from fishjam.events import (
    ServerMessagePeerConnected,
    ServerMessagePeerType,
)
from fishjam.events.allowed_notifications import AllowedNotification

from .config import FISHJAM_ID, FISHJAM_TOKEN, FISHJAM_URL, OPENAI_GREET


def make_notifier(poet: RealtimeSession) -> FishjamNotifier:
    notifier = FishjamNotifier(FISHJAM_ID, FISHJAM_TOKEN, fishjam_url=FISHJAM_URL)

    @notifier.on_server_notification
    async def _(notification: AllowedNotification):
        match notification:
            case ServerMessagePeerConnected(
                peer_type=ServerMessagePeerType.PEER_TYPE_WEBRTC,
            ):
                await handle_peer_connected()

    async def handle_peer_connected():
        await poet.send_message(OPENAI_GREET)

    return notifier
