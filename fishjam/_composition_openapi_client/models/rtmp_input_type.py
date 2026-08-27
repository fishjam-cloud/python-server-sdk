from enum import Enum


class RtmpInputType(str, Enum):
    """None"""

    RTMP_SERVER = "rtmp_server"

    def __str__(self) -> str:
        return str(self.value)
