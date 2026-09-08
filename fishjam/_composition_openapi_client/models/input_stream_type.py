from enum import Enum


class InputStreamType(str, Enum):
    """None"""

    INPUT_STREAM = "input_stream"

    def __str__(self) -> str:
        return str(self.value)
