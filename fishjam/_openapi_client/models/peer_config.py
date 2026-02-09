from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define

from ..models.peer_type import PeerType

if TYPE_CHECKING:
    from ..models.peer_options_agent import PeerOptionsAgent
    from ..models.peer_options_web_rtc import PeerOptionsWebRTC


T = TypeVar("T", bound="PeerConfig")


@_attrs_define
class PeerConfig:
    """Peer configuration

    Attributes:
        options (Union['PeerOptionsAgent', 'PeerOptionsWebRTC']): Peer-specific options
        type_ (PeerType): Peer type Example: webrtc.
    """

    options: Union["PeerOptionsAgent", "PeerOptionsWebRTC"]
    type_: PeerType

    def to_dict(self) -> dict[str, Any]:
        from ..models.peer_options_web_rtc import PeerOptionsWebRTC

        options: dict[str, Any]
        if isinstance(self.options, PeerOptionsWebRTC):
            options = self.options.to_dict()
        else:
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
        from ..models.peer_options_agent import PeerOptionsAgent
        from ..models.peer_options_web_rtc import PeerOptionsWebRTC

        d = dict(src_dict)

        def _parse_options(
            data: object,
        ) -> Union["PeerOptionsAgent", "PeerOptionsWebRTC"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_peer_options_type_0 = PeerOptionsWebRTC.from_dict(
                    data
                )

                return componentsschemas_peer_options_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_peer_options_type_1 = PeerOptionsAgent.from_dict(data)

            return componentsschemas_peer_options_type_1

        options = _parse_options(d.pop("options"))

        type_ = PeerType(d.pop("type"))

        peer_config = cls(
            options=options,
            type_=type_,
        )

        return peer_config
