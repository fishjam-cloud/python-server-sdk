from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnregisterRenderer")


@_attrs_define
class UnregisterRenderer:
    """
    Attributes:
        schedule_time_ms (float | None | Unset): Time in milliseconds when this request should be applied. Value `0`
            represents
            time of the start request.
    """

    schedule_time_ms: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_time_ms: float | None | Unset
        if isinstance(self.schedule_time_ms, Unset):
            schedule_time_ms = UNSET
        else:
            schedule_time_ms = self.schedule_time_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_time_ms is not UNSET:
            field_dict["schedule_time_ms"] = schedule_time_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_schedule_time_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        schedule_time_ms = _parse_schedule_time_ms(d.pop("schedule_time_ms", UNSET))

        unregister_renderer = cls(
            schedule_time_ms=schedule_time_ms,
        )

        unregister_renderer.additional_properties = d
        return unregister_renderer

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
