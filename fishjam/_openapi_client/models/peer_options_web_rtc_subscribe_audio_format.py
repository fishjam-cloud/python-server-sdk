from enum import Enum


class PeerOptionsWebRTCSubscribeAudioFormat(str, Enum):
    """The format to use for the output audio"""

    PCM16 = "pcm16"

    def __str__(self) -> str:
        return str(self.value)
