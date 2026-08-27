from enum import Enum


class WhepInputType(str, Enum):
    """None"""

    WHEP_CLIENT = "whep_client"

    def __str__(self) -> str:
        return str(self.value)
