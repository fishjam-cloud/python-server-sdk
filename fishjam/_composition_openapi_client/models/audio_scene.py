from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.audio_scene_input import AudioSceneInput


T = TypeVar("T", bound="AudioScene")


@_attrs_define
class AudioScene:
    """
    Attributes:
        inputs (list[AudioSceneInput]):
    """

    inputs: list[AudioSceneInput]

    def to_dict(self) -> dict[str, Any]:
        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "inputs": inputs,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audio_scene_input import AudioSceneInput

        d = dict(src_dict)
        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in _inputs:
            inputs_item = AudioSceneInput.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        audio_scene = cls(
            inputs=inputs,
        )

        return audio_scene
