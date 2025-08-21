from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.peer_type import PeerType

if TYPE_CHECKING:
    from ..models.peer_options_agent import PeerOptionsAgent
    from ..models.peer_options_web_rtc import PeerOptionsWebRTC


T = TypeVar("T", bound="AddPeerJsonBody")


@_attrs_define
class AddPeerJsonBody:
    """ """

    options: Union["PeerOptionsAgent", "PeerOptionsWebRTC"]
    """Peer-specific options"""
    type: PeerType
    """Peer type"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        from ..models.peer_options_web_rtc import PeerOptionsWebRTC

        options: Dict[str, Any]

        if isinstance(self.options, PeerOptionsWebRTC):
            options = self.options.to_dict()

        else:
            options = self.options.to_dict()

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "options": options,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.peer_options_agent import PeerOptionsAgent
        from ..models.peer_options_web_rtc import PeerOptionsWebRTC

        d = src_dict.copy()

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

        type = PeerType(d.pop("type"))

        add_peer_json_body = cls(
            options=options,
            type=type,
        )

        add_peer_json_body.additional_properties = d
        return add_peer_json_body

    @property
    def additional_keys(self) -> List[str]:
        """@private"""
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
