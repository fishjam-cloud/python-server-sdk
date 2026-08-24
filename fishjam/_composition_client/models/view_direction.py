from enum import Enum


class ViewDirection(str, Enum):
    """None"""

    COLUMN = "column"
    ROW = "row"

    def __str__(self) -> str:
        return str(self.value)
