from enum import Enum


class OpusEncoderPreset(str, Enum):
    """None"""

    LOWEST_LATENCY = "lowest_latency"
    QUALITY = "quality"
    VOIP = "voip"

    def __str__(self) -> str:
        return str(self.value)
