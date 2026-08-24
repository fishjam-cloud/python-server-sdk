from enum import Enum


class TextWrapMode(str, Enum):
    """None"""

    GLYPH = "glyph"
    NONE = "none"
    WORD = "word"

    def __str__(self) -> str:
        return str(self.value)
