from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_spec_gif_asset_type import ImageSpecGifAssetType

T = TypeVar("T", bound="ImageSpecGif")


@_attrs_define
class ImageSpecGif:
    """
    Attributes:
        url (str):
        asset_type (ImageSpecGifAssetType):
    """

    url: str
    asset_type: ImageSpecGifAssetType
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

        asset_type = ImageSpecGifAssetType(d.pop("asset_type"))

        image_spec_gif = cls(
            url=url,
            asset_type=asset_type,
        )

        image_spec_gif.additional_properties = d
        return image_spec_gif

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
