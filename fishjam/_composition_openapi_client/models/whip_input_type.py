from enum import Enum


class WhipInputType(str, Enum):
    """None"""

    WHIP_SERVER = "whip_server"

    def __str__(self) -> str:
        return str(self.value)
