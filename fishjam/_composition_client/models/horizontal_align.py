from enum import Enum


class HorizontalAlign(str, Enum):
    """None"""

    CENTER = "center"
    JUSTIFIED = "justified"
    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
