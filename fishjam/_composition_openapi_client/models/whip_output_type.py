from enum import Enum


class WhipOutputType(str, Enum):
    """None"""

    WHIP_CLIENT = "whip_client"

    def __str__(self) -> str:
        return str(self.value)
