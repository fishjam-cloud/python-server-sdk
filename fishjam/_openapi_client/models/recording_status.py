from enum import Enum


class RecordingStatus(str, Enum):
    """Lifecycle status of a recording"""

    ACTIVE = "active"
    AVAILABLE = "available"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
