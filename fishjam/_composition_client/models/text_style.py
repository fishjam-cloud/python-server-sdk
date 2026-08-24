from enum import Enum


class TextStyle(str, Enum):
    """None"""

    ITALIC = "italic"
    NORMAL = "normal"
    OBLIQUE = "oblique"

    def __str__(self) -> str:
        return str(self.value)
