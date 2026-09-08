from enum import Enum


class Overflow(str, Enum):
    """None"""

    FIT = "fit"
    HIDDEN = "hidden"
    VISIBLE = "visible"

    def __str__(self) -> str:
        return str(self.value)
