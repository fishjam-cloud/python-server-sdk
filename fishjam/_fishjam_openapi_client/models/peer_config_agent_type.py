from enum import Enum


class PeerConfigAgentType(str, Enum):
    """Peer type"""

    AGENT = "agent"

    def __str__(self) -> str:
        return str(self.value)
