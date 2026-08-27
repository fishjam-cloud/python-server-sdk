from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.opus_encoder_preset import OpusEncoderPreset
from ..models.whip_audio_encoder_options_opus_type import (
    WhipAudioEncoderOptionsOpusType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WhipAudioEncoderOptionsOpus")


@_attrs_define
class WhipAudioEncoderOptionsOpus:
    """
    Attributes:
        type_ (WhipAudioEncoderOptionsOpusType):
        preset (None | OpusEncoderPreset | Unset):
        sample_rate (int | None | Unset): (**default=`48000`**) Sample rate. Allowed values: [8000, 16000, 24000,
            48000].
        forward_error_correction (bool | None | Unset): (**default=`false`**) Specifies if forward error correction
            (FEC) should be used.
    """

    type_: WhipAudioEncoderOptionsOpusType
    preset: None | OpusEncoderPreset | Unset = UNSET
    sample_rate: int | None | Unset = UNSET
    forward_error_correction: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        preset: None | str | Unset
        if isinstance(self.preset, Unset):
            preset = UNSET
        elif isinstance(self.preset, OpusEncoderPreset):
            preset = self.preset.value
        else:
            preset = self.preset

        sample_rate: int | None | Unset
        if isinstance(self.sample_rate, Unset):
            sample_rate = UNSET
        else:
            sample_rate = self.sample_rate

        forward_error_correction: bool | None | Unset
        if isinstance(self.forward_error_correction, Unset):
            forward_error_correction = UNSET
        else:
            forward_error_correction = self.forward_error_correction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if preset is not UNSET:
            field_dict["preset"] = preset
        if sample_rate is not UNSET:
            field_dict["sample_rate"] = sample_rate
        if forward_error_correction is not UNSET:
            field_dict["forward_error_correction"] = forward_error_correction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = WhipAudioEncoderOptionsOpusType(d.pop("type"))

        def _parse_preset(data: object) -> None | OpusEncoderPreset | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preset_type_1 = OpusEncoderPreset(data)

                return preset_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OpusEncoderPreset | Unset, data)

        preset = _parse_preset(d.pop("preset", UNSET))

        def _parse_sample_rate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sample_rate = _parse_sample_rate(d.pop("sample_rate", UNSET))

        def _parse_forward_error_correction(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        forward_error_correction = _parse_forward_error_correction(
            d.pop("forward_error_correction", UNSET)
        )

        whip_audio_encoder_options_opus = cls(
            type_=type_,
            preset=preset,
            sample_rate=sample_rate,
            forward_error_correction=forward_error_correction,
        )

        whip_audio_encoder_options_opus.additional_properties = d
        return whip_audio_encoder_options_opus

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
