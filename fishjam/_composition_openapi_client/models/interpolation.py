from enum import Enum


class Interpolation(str, Enum):
    """None"""

    LINEAR = "linear"
    SPRING = "spring"

    def __str__(self) -> str:
        return str(self.value)
