from enum import Enum


class TransportProtocol(str, Enum):
    """None"""

    TCP_SERVER = "tcp_server"
    UDP = "udp"

    def __str__(self) -> str:
        return str(self.value)
