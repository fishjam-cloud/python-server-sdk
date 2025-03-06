from enum import Enum


class RoomConfigRoomType(str, Enum):
    """None"""

    AUDIO_ONLY = "audio_only"
    FULL_FEATURE = "full_feature"

    def __str__(self) -> str:
        return str(self.value)
