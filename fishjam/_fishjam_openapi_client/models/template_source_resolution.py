from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TemplateSourceResolution")


@_attrs_define
class TemplateSourceResolution:
    """Resolution the scene is rendered at. Defaults to 1280x720.

    Attributes:
        height (int):
        width (int):
    """

    height: int
    width: int

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        width = self.width

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "height": height,
            "width": width,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height")

        width = d.pop("width")

        template_source_resolution = cls(
            height=height,
            width=width,
        )

        return template_source_resolution
