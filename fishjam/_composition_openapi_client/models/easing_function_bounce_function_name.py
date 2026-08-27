from enum import Enum


class EasingFunctionBounceFunctionName(str, Enum):
    """None"""

    BOUNCE = "bounce"

    def __str__(self) -> str:
        return str(self.value)
