from enum import Enum


class ViewType(str, Enum):
    """None"""

    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
