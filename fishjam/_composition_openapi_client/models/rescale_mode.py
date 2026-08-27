from enum import Enum


class RescaleMode(str, Enum):
    """None"""

    FILL = "fill"
    FIT = "fit"

    def __str__(self) -> str:
        return str(self.value)
