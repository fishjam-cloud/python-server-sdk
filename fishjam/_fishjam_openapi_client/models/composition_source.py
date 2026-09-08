from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompositionSource")


@_attrs_define
class CompositionSource:
    """Recording source coming from composition

    Attributes:
        composition_url (str): URL of the composition to record
        output_id (str): Id of the output being recorded
        scale_ratio (float | Unset): Scale factor for the recording relative to the source output (>0; may upscale or
            downscale). Defaults to 1. Default: 1.0.
    """

    composition_url: str
    output_id: str
    scale_ratio: float | Unset = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        composition_url = self.composition_url

        output_id = self.output_id

        scale_ratio = self.scale_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "compositionURL": composition_url,
            "outputId": output_id,
        })
        if scale_ratio is not UNSET:
            field_dict["scaleRatio"] = scale_ratio

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        composition_url = d.pop("compositionURL")

        output_id = d.pop("outputId")

        scale_ratio = d.pop("scaleRatio", UNSET)

        composition_source = cls(
            composition_url=composition_url,
            output_id=output_id,
            scale_ratio=scale_ratio,
        )

        composition_source.additional_properties = d
        return composition_source

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
