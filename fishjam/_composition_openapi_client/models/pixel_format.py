from enum import Enum


class PixelFormat(str, Enum):
    """None"""

    YUV420P = "yuv420p"
    YUV422P = "yuv422p"
    YUV444P = "yuv444p"

    def __str__(self) -> str:
        return str(self.value)
