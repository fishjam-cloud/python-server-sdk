from enum import Enum


class TilesType(str, Enum):
    """None"""

    TILES = "tiles"

    def __str__(self) -> str:
        return str(self.value)
