from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_spec_png_asset_type import ImageSpecPngAssetType

T = TypeVar("T", bound="ImageSpecPng")


@_attrs_define
class ImageSpecPng:
    """
    Attributes:
        url (str):
        asset_type (ImageSpecPngAssetType):
    """

    url: str
    asset_type: ImageSpecPngAssetType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        asset_type = self.asset_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "url": url,
            "asset_type": asset_type,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        asset_type = ImageSpecPngAssetType(d.pop("asset_type"))

        image_spec_png = cls(
            url=url,
            asset_type=asset_type,
        )

        image_spec_png.additional_properties = d
        return image_spec_png

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
