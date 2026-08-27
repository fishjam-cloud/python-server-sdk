from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Image")


@_attrs_define
class Image:
    """
    Attributes:
        image_id (str):
        type_ (ImageType):
        id (None | str | Unset):
        width (float | None | Unset): Width of the image in pixels.
            If `height` is not explicitly provided, the image will automatically adjust its height to maintain its original
            aspect ratio relative to the width.
        height (float | None | Unset): Height of the image in pixels.
            If `width` is not explicitly provided, the image will automatically adjust its width to maintain its original
            aspect ratio relative to the height.
    """

    image_id: str
    type_: ImageType
    id: None | str | Unset = UNSET
    width: float | None | Unset = UNSET
    height: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        image_id = self.image_id

        type_ = self.type_.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        width: float | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: float | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "image_id": image_id,
            "type": type_,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_id = d.pop("image_id")

        type_ = ImageType(d.pop("type"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_width(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))

        def _parse_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        image = cls(
            image_id=image_id,
            type_=type_,
            id=id,
            width=width,
            height=height,
        )

        return image
