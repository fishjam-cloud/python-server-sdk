from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_source_resolution import TemplateSourceResolution


T = TypeVar("T", bound="TemplateSource")


@_attrs_define
class TemplateSource:
    """Recording source that renders its own scene from a template, rather than cloning an existing output of the
    composition

        Attributes:
            composition_url (str): URL of the composition to record
            audio (bool | Unset): Whether the recording captures audio. Defaults to true. Default: True.
            resolution (TemplateSourceResolution | Unset): Resolution the scene is rendered at. Defaults to 1280x720.
    """

    composition_url: str
    audio: bool | Unset = True
    resolution: TemplateSourceResolution | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        composition_url = self.composition_url

        audio = self.audio

        resolution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "compositionURL": composition_url,
        })
        if audio is not UNSET:
            field_dict["audio"] = audio
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_source_resolution import TemplateSourceResolution

        d = dict(src_dict)
        composition_url = d.pop("compositionURL")

        audio = d.pop("audio", UNSET)

        _resolution = d.pop("resolution", UNSET)
        resolution: TemplateSourceResolution | Unset
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = TemplateSourceResolution.from_dict(_resolution)

        template_source = cls(
            composition_url=composition_url,
            audio=audio,
            resolution=resolution,
        )

        return template_source
