from enum import Enum


class ImageSpecAutoAssetType(str, Enum):
    """None"""

    AUTO = "auto"

    def __str__(self) -> str:
        return str(self.value)
