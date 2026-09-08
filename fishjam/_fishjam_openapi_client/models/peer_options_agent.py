from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.subscribe_mode import SubscribeMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_output import AgentOutput


T = TypeVar("T", bound="PeerOptionsAgent")


@_attrs_define
class PeerOptionsAgent:
    """Options specific to the Agent peer

    Attributes:
        output (AgentOutput | Unset): Output audio options
        subscribe_mode (SubscribeMode | Unset): Configuration of peer's subscribing policy
    """

    output: AgentOutput | Unset = UNSET
    subscribe_mode: SubscribeMode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        subscribe_mode: str | Unset = UNSET
        if not isinstance(self.subscribe_mode, Unset):
            subscribe_mode = self.subscribe_mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if output is not UNSET:
            field_dict["output"] = output
        if subscribe_mode is not UNSET:
            field_dict["subscribeMode"] = subscribe_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_output import AgentOutput

        d = dict(src_dict)
        _output = d.pop("output", UNSET)
        output: AgentOutput | Unset
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = AgentOutput.from_dict(_output)

        _subscribe_mode = d.pop("subscribeMode", UNSET)
        subscribe_mode: SubscribeMode | Unset
        if isinstance(_subscribe_mode, Unset):
            subscribe_mode = UNSET
        else:
            subscribe_mode = SubscribeMode(_subscribe_mode)

        peer_options_agent = cls(
            output=output,
            subscribe_mode=subscribe_mode,
        )

        return peer_options_agent
