from enum import Enum


class AudioChannels(str, Enum):
    """None"""

    MONO = "mono"
    STEREO = "stereo"

    def __str__(self) -> str:
        return str(self.value)
