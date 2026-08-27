from enum import Enum


class H264EncoderPreset(str, Enum):
    """None"""

    FAST = "fast"
    FASTER = "faster"
    MEDIUM = "medium"
    PLACEBO = "placebo"
    SLOW = "slow"
    SLOWER = "slower"
    SUPERFAST = "superfast"
    ULTRAFAST = "ultrafast"
    VERYFAST = "veryfast"
    VERYSLOW = "veryslow"

    def __str__(self) -> str:
        return str(self.value)
