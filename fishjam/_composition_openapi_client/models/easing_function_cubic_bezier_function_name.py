from enum import Enum


class EasingFunctionCubicBezierFunctionName(str, Enum):
    """None"""

    CUBIC_BEZIER = "cubic_bezier"

    def __str__(self) -> str:
        return str(self.value)
