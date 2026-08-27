from enum import Enum


class ImageSpecSvgAssetType(str, Enum):
    """None"""

    SVG = "svg"

    def __str__(self) -> str:
        return str(self.value)
