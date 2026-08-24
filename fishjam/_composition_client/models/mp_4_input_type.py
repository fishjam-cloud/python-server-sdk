from enum import Enum


class Mp4InputType(str, Enum):
    """None"""

    MP4 = "mp4"

    def __str__(self) -> str:
        return str(self.value)
