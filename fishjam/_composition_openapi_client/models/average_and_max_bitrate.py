from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AverageAndMaxBitrate")


@_attrs_define
class AverageAndMaxBitrate:
    """
    Attributes:
        average_bitrate (int): Average bitrate measured in bits/second. Encoder will try to keep the bitrate around the
            provided average,
            but may temporarily increase it to the provided max bitrate.
        max_bitrate (int): Max bitrate measured in bits/second.
    """

    average_bitrate: int
    max_bitrate: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average_bitrate = self.average_bitrate

        max_bitrate = self.max_bitrate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "average_bitrate": average_bitrate,
            "max_bitrate": max_bitrate,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        average_bitrate = d.pop("average_bitrate")

        max_bitrate = d.pop("max_bitrate")

        average_and_max_bitrate = cls(
            average_bitrate=average_bitrate,
            max_bitrate=max_bitrate,
        )

        average_and_max_bitrate.additional_properties = d
        return average_and_max_bitrate

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
