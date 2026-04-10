from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.audio_format import AudioFormat
from ..models.audio_sample_rate import AudioSampleRate
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentOutput")


@_attrs_define
class AgentOutput:
    """Output audio options

    Attributes:
        audio_format (AudioFormat | Unset): The format of the output audio Example: pcm16.
        audio_sample_rate (AudioSampleRate | Unset): The sample rate of the output audio Example: 16000.
    """

    audio_format: AudioFormat | Unset = UNSET
    audio_sample_rate: AudioSampleRate | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        audio_format: str | Unset = UNSET
        if not isinstance(self.audio_format, Unset):
            audio_format = self.audio_format.value

        audio_sample_rate: int | Unset = UNSET
        if not isinstance(self.audio_sample_rate, Unset):
            audio_sample_rate = self.audio_sample_rate.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if audio_format is not UNSET:
            field_dict["audioFormat"] = audio_format
        if audio_sample_rate is not UNSET:
            field_dict["audioSampleRate"] = audio_sample_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _audio_format = d.pop("audioFormat", UNSET)
        audio_format: AudioFormat | Unset
        if isinstance(_audio_format, Unset):
            audio_format = UNSET
        else:
            audio_format = AudioFormat(_audio_format)

        _audio_sample_rate = d.pop("audioSampleRate", UNSET)
        audio_sample_rate: AudioSampleRate | Unset
        if isinstance(_audio_sample_rate, Unset):
            audio_sample_rate = UNSET
        else:
            audio_sample_rate = AudioSampleRate(_audio_sample_rate)

        agent_output = cls(
            audio_format=audio_format,
            audio_sample_rate=audio_sample_rate,
        )

        return agent_output
