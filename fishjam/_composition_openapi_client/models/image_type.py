from enum import Enum


class ImageType(str, Enum):
    """None"""

    IMAGE = "image"

    def __str__(self) -> str:
        return str(self.value)
