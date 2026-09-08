from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.audio_channels import AudioChannels
from ..models.audio_mixing_strategy import AudioMixingStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audio_scene import AudioScene
    from ..models.output_end_condition import OutputEndCondition
    from ..models.whip_audio_encoder_options_any import WhipAudioEncoderOptionsAny
    from ..models.whip_audio_encoder_options_opus import WhipAudioEncoderOptionsOpus


T = TypeVar("T", bound="OutputWhipAudioOptions")


@_attrs_define
class OutputWhipAudioOptions:
    """
    Attributes:
        initial (AudioScene):
        mixing_strategy (AudioMixingStrategy | None | Unset):
        send_eos_when (None | OutputEndCondition | Unset):
        channels (AudioChannels | None | Unset):
        encoder_preferences (list[WhipAudioEncoderOptionsAny | WhipAudioEncoderOptionsOpus] | None | Unset): Codec
            preferences list.
    """

    initial: AudioScene
    mixing_strategy: AudioMixingStrategy | None | Unset = UNSET
    send_eos_when: None | OutputEndCondition | Unset = UNSET
    channels: AudioChannels | None | Unset = UNSET
    encoder_preferences: (
        list[WhipAudioEncoderOptionsAny | WhipAudioEncoderOptionsOpus] | None | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.output_end_condition import OutputEndCondition
        from ..models.whip_audio_encoder_options_opus import WhipAudioEncoderOptionsOpus

        initial = self.initial.to_dict()

        mixing_strategy: None | str | Unset
        if isinstance(self.mixing_strategy, Unset):
            mixing_strategy = UNSET
        elif isinstance(self.mixing_strategy, AudioMixingStrategy):
            mixing_strategy = self.mixing_strategy.value
        else:
            mixing_strategy = self.mixing_strategy

        send_eos_when: dict[str, Any] | None | Unset
        if isinstance(self.send_eos_when, Unset):
            send_eos_when = UNSET
        elif isinstance(self.send_eos_when, OutputEndCondition):
            send_eos_when = self.send_eos_when.to_dict()
        else:
            send_eos_when = self.send_eos_when

        channels: None | str | Unset
        if isinstance(self.channels, Unset):
            channels = UNSET
        elif isinstance(self.channels, AudioChannels):
            channels = self.channels.value
        else:
            channels = self.channels

        encoder_preferences: list[dict[str, Any]] | None | Unset
        if isinstance(self.encoder_preferences, Unset):
            encoder_preferences = UNSET
        elif isinstance(self.encoder_preferences, list):
            encoder_preferences = []
            for encoder_preferences_type_0_item_data in self.encoder_preferences:
                encoder_preferences_type_0_item: dict[str, Any]
                if isinstance(
                    encoder_preferences_type_0_item_data, WhipAudioEncoderOptionsOpus
                ):
                    encoder_preferences_type_0_item = (
                        encoder_preferences_type_0_item_data.to_dict()
                    )
                else:
                    encoder_preferences_type_0_item = (
                        encoder_preferences_type_0_item_data.to_dict()
                    )

                encoder_preferences.append(encoder_preferences_type_0_item)

        else:
            encoder_preferences = self.encoder_preferences

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "initial": initial,
        })
        if mixing_strategy is not UNSET:
            field_dict["mixing_strategy"] = mixing_strategy
        if send_eos_when is not UNSET:
            field_dict["send_eos_when"] = send_eos_when
        if channels is not UNSET:
            field_dict["channels"] = channels
        if encoder_preferences is not UNSET:
            field_dict["encoder_preferences"] = encoder_preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audio_scene import AudioScene
        from ..models.output_end_condition import OutputEndCondition
        from ..models.whip_audio_encoder_options_any import WhipAudioEncoderOptionsAny
        from ..models.whip_audio_encoder_options_opus import WhipAudioEncoderOptionsOpus

        d = dict(src_dict)
        initial = AudioScene.from_dict(d.pop("initial"))

        def _parse_mixing_strategy(data: object) -> AudioMixingStrategy | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mixing_strategy_type_1 = AudioMixingStrategy(data)

                return mixing_strategy_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AudioMixingStrategy | None | Unset, data)

        mixing_strategy = _parse_mixing_strategy(d.pop("mixing_strategy", UNSET))

        def _parse_send_eos_when(data: object) -> None | OutputEndCondition | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                send_eos_when_type_1 = OutputEndCondition.from_dict(data)

                return send_eos_when_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OutputEndCondition | Unset, data)

        send_eos_when = _parse_send_eos_when(d.pop("send_eos_when", UNSET))

        def _parse_channels(data: object) -> AudioChannels | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                channels_type_1 = AudioChannels(data)

                return channels_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AudioChannels | None | Unset, data)

        channels = _parse_channels(d.pop("channels", UNSET))

        def _parse_encoder_preferences(
            data: object,
        ) -> (
            list[WhipAudioEncoderOptionsAny | WhipAudioEncoderOptionsOpus]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                encoder_preferences_type_0 = []
                _encoder_preferences_type_0 = data
                for encoder_preferences_type_0_item_data in _encoder_preferences_type_0:

                    def _parse_encoder_preferences_type_0_item(
                        data: object,
                    ) -> WhipAudioEncoderOptionsAny | WhipAudioEncoderOptionsOpus:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_whip_audio_encoder_options_whip_audio_encoder_options_opus = WhipAudioEncoderOptionsOpus.from_dict(
                                data
                            )

                            return componentsschemas_whip_audio_encoder_options_whip_audio_encoder_options_opus
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_whip_audio_encoder_options_whip_audio_encoder_options_any = WhipAudioEncoderOptionsAny.from_dict(
                            data
                        )

                        return componentsschemas_whip_audio_encoder_options_whip_audio_encoder_options_any

                    encoder_preferences_type_0_item = (
                        _parse_encoder_preferences_type_0_item(
                            encoder_preferences_type_0_item_data
                        )
                    )

                    encoder_preferences_type_0.append(encoder_preferences_type_0_item)

                return encoder_preferences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[WhipAudioEncoderOptionsAny | WhipAudioEncoderOptionsOpus]
                | None
                | Unset,
                data,
            )

        encoder_preferences = _parse_encoder_preferences(
            d.pop("encoder_preferences", UNSET)
        )

        output_whip_audio_options = cls(
            initial=initial,
            mixing_strategy=mixing_strategy,
            send_eos_when=send_eos_when,
            channels=channels,
            encoder_preferences=encoder_preferences,
        )

        return output_whip_audio_options
