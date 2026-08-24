from enum import Enum


class RtmpOutputType(str, Enum):
    """None"""

    RTMP_CLIENT = "rtmp_client"

    def __str__(self) -> str:
        return str(self.value)
