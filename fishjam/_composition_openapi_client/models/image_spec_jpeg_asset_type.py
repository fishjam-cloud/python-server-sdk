from enum import Enum


class ImageSpecJpegAssetType(str, Enum):
    """None"""

    JPEG = "jpeg"

    def __str__(self) -> str:
        return str(self.value)
