from enum import Enum


class ImageSpecPngAssetType(str, Enum):
    """None"""

    PNG = "png"

    def __str__(self) -> str:
        return str(self.value)
