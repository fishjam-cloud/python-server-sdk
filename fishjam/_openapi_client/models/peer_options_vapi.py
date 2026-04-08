from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define

from ..models.subscribe_mode import SubscribeMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeerOptionsVapi")


@_attrs_define
class PeerOptionsVapi:
    """Options specific to the VAPI peer

    Attributes:
        api_key (str): VAPI API key
        call_id (str): VAPI call ID
        subscribe_mode (Union[Unset, SubscribeMode]): Configuration of peer's subscribing policy
    """

    api_key: str
    call_id: str
    subscribe_mode: Union[Unset, SubscribeMode] = UNSET

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        call_id = self.call_id

        subscribe_mode: Union[Unset, str] = UNSET
        if not isinstance(self.subscribe_mode, Unset):
            subscribe_mode = self.subscribe_mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "apiKey": api_key,
            "callId": call_id,
        })
        if subscribe_mode is not UNSET:
            field_dict["subscribeMode"] = subscribe_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        call_id = d.pop("callId")

        _subscribe_mode = d.pop("subscribeMode", UNSET)
        subscribe_mode: Union[Unset, SubscribeMode]
        if isinstance(_subscribe_mode, Unset):
            subscribe_mode = UNSET
        else:
            subscribe_mode = SubscribeMode(_subscribe_mode)

        peer_options_vapi = cls(
            api_key=api_key,
            call_id=call_id,
            subscribe_mode=subscribe_mode,
        )

        return peer_options_vapi
