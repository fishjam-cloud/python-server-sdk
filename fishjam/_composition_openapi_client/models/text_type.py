from enum import Enum


class TextType(str, Enum):
    """None"""

    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
