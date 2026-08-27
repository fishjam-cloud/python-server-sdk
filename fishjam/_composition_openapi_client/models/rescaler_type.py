from enum import Enum


class RescalerType(str, Enum):
    """None"""

    RESCALER = "rescaler"

    def __str__(self) -> str:
        return str(self.value)
