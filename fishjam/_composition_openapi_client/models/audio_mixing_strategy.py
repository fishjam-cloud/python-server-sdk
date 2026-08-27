from enum import Enum


class AudioMixingStrategy(str, Enum):
    """None"""

    SUM_CLIP = "sum_clip"
    SUM_SCALE = "sum_scale"

    def __str__(self) -> str:
        return str(self.value)
