from enum import Enum


class TextWeight(str, Enum):
    """Font weight, based on the [OpenType specification](https://learn.microsoft.com/en-gb/typography/opentype/spec/os2#usweightclass)."""

    BLACK = "black"
    BOLD = "bold"
    EXTRA_BOLD = "extra_bold"
    EXTRA_LIGHT = "extra_light"
    LIGHT = "light"
    MEDIUM = "medium"
    NORMAL = "normal"
    SEMI_BOLD = "semi_bold"
    THIN = "thin"

    def __str__(self) -> str:
        return str(self.value)
