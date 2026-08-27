from enum import Enum


class PeerConfigWebRTCType(str, Enum):
    """Peer type"""

    WEBRTC = "webrtc"

    def __str__(self) -> str:
        return str(self.value)
