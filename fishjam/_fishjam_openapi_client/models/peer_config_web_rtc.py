from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.peer_config_web_rtc_type import PeerConfigWebRTCType

if TYPE_CHECKING:
    from ..models.peer_options_web_rtc import PeerOptionsWebRTC


T = TypeVar("T", bound="PeerConfigWebRTC")


@_attrs_define
class PeerConfigWebRTC:
    """Configuration of a webrtc peer

    Attributes:
        options (PeerOptionsWebRTC): Options specific to the WebRTC peer
        type_ (PeerConfigWebRTCType): Peer type
    """

    options: PeerOptionsWebRTC
    type_: PeerConfigWebRTCType

    def to_dict(self) -> dict[str, Any]:
        options = self.options.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "options": options,
            "type": type_,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.peer_options_web_rtc import PeerOptionsWebRTC

        d = dict(src_dict)
        options = PeerOptionsWebRTC.from_dict(d.pop("options"))

        type_ = PeerConfigWebRTCType(d.pop("type"))

        peer_config_web_rtc = cls(
            options=options,
            type_=type_,
        )

        return peer_config_web_rtc
