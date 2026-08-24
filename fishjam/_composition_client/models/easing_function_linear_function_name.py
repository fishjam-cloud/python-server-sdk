from enum import Enum


class EasingFunctionLinearFunctionName(str, Enum):
    """None"""

    LINEAR = "linear"

    def __str__(self) -> str:
        return str(self.value)
