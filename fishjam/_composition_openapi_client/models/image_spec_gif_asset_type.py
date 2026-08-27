from enum import Enum


class ImageSpecGifAssetType(str, Enum):
    """None"""

    GIF = "gif"

    def __str__(self) -> str:
        return str(self.value)
