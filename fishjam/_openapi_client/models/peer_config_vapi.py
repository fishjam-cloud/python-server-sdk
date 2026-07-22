from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.peer_config_vapi_type import PeerConfigVAPIType

if TYPE_CHECKING:
    from ..models.peer_options_vapi import PeerOptionsVapi


T = TypeVar("T", bound="PeerConfigVAPI")


@_attrs_define
class PeerConfigVAPI:
    """Configuration of a VAPI peer

    Attributes:
        options (PeerOptionsVapi): Options specific to the VAPI peer
        type_ (PeerConfigVAPIType): Peer type
    """

    options: PeerOptionsVapi
    type_: PeerConfigVAPIType

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
        from ..models.peer_options_vapi import PeerOptionsVapi

        d = dict(src_dict)
        options = PeerOptionsVapi.from_dict(d.pop("options"))

        type_ = PeerConfigVAPIType(d.pop("type"))

        peer_config_vapi = cls(
            options=options,
            type_=type_,
        )

        return peer_config_vapi
