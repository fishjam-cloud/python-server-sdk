from enum import Enum


class WhipAudioEncoderOptionsAnyType(str, Enum):
    """None"""

    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)
