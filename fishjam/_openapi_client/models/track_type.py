from enum import Enum


class TrackType(str, Enum):
    """Media type carried by the track"""

    AUDIO = "audio"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
