from enum import Enum


class WhipAudioEncoderOptionsOpusType(str, Enum):
    """None"""

    OPUS = "opus"

    def __str__(self) -> str:
        return str(self.value)
