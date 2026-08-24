from enum import Enum


class VerticalAlign(str, Enum):
    """None"""

    BOTTOM = "bottom"
    CENTER = "center"
    JUSTIFIED = "justified"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
