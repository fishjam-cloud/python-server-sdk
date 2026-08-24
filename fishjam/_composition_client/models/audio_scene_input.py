from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AudioSceneInput")


@_attrs_define
class AudioSceneInput:
    """
    Attributes:
        input_id (str):
        volume (float | None | Unset): (**default=`1.0`**) float in `[0, 2]` range representing input volume
    """

    input_id: str
    volume: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        input_id = self.input_id

        volume: float | None | Unset
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "input_id": input_id,
        })
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_id = d.pop("input_id")

        def _parse_volume(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        volume = _parse_volume(d.pop("volume", UNSET))

        audio_scene_input = cls(
            input_id=input_id,
            volume=volume,
        )

        return audio_scene_input
