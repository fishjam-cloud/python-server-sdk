from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendCompositionEventBody")


@_attrs_define
class SendCompositionEventBody:
    """
    Attributes:
        event_name (str): Name of the event delivered to the composition's templates. Example: START_LIVE.
        data (Any | Unset): Optional arbitrary JSON payload delivered with the event.
    """

    event_name: str
    data: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        event_name = self.event_name

        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "event_name": event_name,
        })
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_name = d.pop("event_name")

        data = d.pop("data", UNSET)

        send_composition_event_body = cls(
            event_name=event_name,
            data=data,
        )

        return send_composition_event_body
