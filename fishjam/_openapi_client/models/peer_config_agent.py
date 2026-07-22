from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.peer_config_agent_type import PeerConfigAgentType

if TYPE_CHECKING:
    from ..models.peer_options_agent import PeerOptionsAgent


T = TypeVar("T", bound="PeerConfigAgent")


@_attrs_define
class PeerConfigAgent:
    """Configuration of an agent peer

    Attributes:
        options (PeerOptionsAgent): Options specific to the Agent peer
        type_ (PeerConfigAgentType): Peer type
    """

    options: PeerOptionsAgent
    type_: PeerConfigAgentType

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
        from ..models.peer_options_agent import PeerOptionsAgent

        d = dict(src_dict)
        options = PeerOptionsAgent.from_dict(d.pop("options"))

        type_ = PeerConfigAgentType(d.pop("type"))

        peer_config_agent = cls(
            options=options,
            type_=type_,
        )

        return peer_config_agent
