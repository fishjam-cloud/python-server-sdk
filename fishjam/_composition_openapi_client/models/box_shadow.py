from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BoxShadow")


@_attrs_define
class BoxShadow:
    """
    Attributes:
        offset_x (float | None | Unset):
        offset_y (float | None | Unset):
        color (None | str | Unset):
        blur_radius (float | None | Unset):
    """

    offset_x: float | None | Unset = UNSET
    offset_y: float | None | Unset = UNSET
    color: None | str | Unset = UNSET
    blur_radius: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset_x: float | None | Unset
        if isinstance(self.offset_x, Unset):
            offset_x = UNSET
        else:
            offset_x = self.offset_x

        offset_y: float | None | Unset
        if isinstance(self.offset_y, Unset):
            offset_y = UNSET
        else:
            offset_y = self.offset_y

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        blur_radius: float | None | Unset
        if isinstance(self.blur_radius, Unset):
            blur_radius = UNSET
        else:
            blur_radius = self.blur_radius

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if offset_x is not UNSET:
            field_dict["offset_x"] = offset_x
        if offset_y is not UNSET:
            field_dict["offset_y"] = offset_y
        if color is not UNSET:
            field_dict["color"] = color
        if blur_radius is not UNSET:
            field_dict["blur_radius"] = blur_radius

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_offset_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        offset_x = _parse_offset_x(d.pop("offset_x", UNSET))

        def _parse_offset_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        offset_y = _parse_offset_y(d.pop("offset_y", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_blur_radius(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        blur_radius = _parse_blur_radius(d.pop("blur_radius", UNSET))

        box_shadow = cls(
            offset_x=offset_x,
            offset_y=offset_y,
            color=color,
            blur_radius=blur_radius,
        )

        return box_shadow
