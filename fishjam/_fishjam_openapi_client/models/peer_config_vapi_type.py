from enum import Enum


class PeerConfigVAPIType(str, Enum):
    """Peer type"""

    VAPI = "vapi"

    def __str__(self) -> str:
        return str(self.value)
