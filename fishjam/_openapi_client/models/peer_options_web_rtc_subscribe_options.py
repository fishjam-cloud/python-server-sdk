from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.peer_options_web_rtc_subscribe_options_audio_format import (
    PeerOptionsWebRTCSubscribeOptionsAudioFormat,
)
from ..models.peer_options_web_rtc_subscribe_options_audio_sample_rate import (
    PeerOptionsWebRTCSubscribeOptionsAudioSampleRate,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeerOptionsWebRTCSubscribeOptions")


@_attrs_define
class PeerOptionsWebRTCSubscribeOptions:
    """Configuration of server-side subscriptions to the peer's tracks

    Example:
        {'audioFormat': 'pcm16'}

    """

    audio_format: Union[
        Unset, PeerOptionsWebRTCSubscribeOptionsAudioFormat
    ] = PeerOptionsWebRTCSubscribeOptionsAudioFormat.PCM16
    """The format of the output audio"""
    audio_sample_rate: Union[
        Unset, PeerOptionsWebRTCSubscribeOptionsAudioSampleRate
    ] = PeerOptionsWebRTCSubscribeOptionsAudioSampleRate.VALUE_16000
    """The sample rate of the output audio"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        audio_format: Union[Unset, str] = UNSET
        if not isinstance(self.audio_format, Unset):
            audio_format = self.audio_format.value

        audio_sample_rate: Union[Unset, int] = UNSET
        if not isinstance(self.audio_sample_rate, Unset):
            audio_sample_rate = self.audio_sample_rate.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if audio_format is not UNSET:
            field_dict["audioFormat"] = audio_format
        if audio_sample_rate is not UNSET:
            field_dict["audioSampleRate"] = audio_sample_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        _audio_format = d.pop("audioFormat", UNSET)
        audio_format: Union[Unset, PeerOptionsWebRTCSubscribeOptionsAudioFormat]
        if isinstance(_audio_format, Unset):
            audio_format = UNSET
        else:
            audio_format = PeerOptionsWebRTCSubscribeOptionsAudioFormat(_audio_format)

        _audio_sample_rate = d.pop("audioSampleRate", UNSET)
        audio_sample_rate: Union[
            Unset, PeerOptionsWebRTCSubscribeOptionsAudioSampleRate
        ]
        if isinstance(_audio_sample_rate, Unset):
            audio_sample_rate = UNSET
        else:
            audio_sample_rate = PeerOptionsWebRTCSubscribeOptionsAudioSampleRate(
                _audio_sample_rate
            )

        peer_options_web_rtc_subscribe_options = cls(
            audio_format=audio_format,
            audio_sample_rate=audio_sample_rate,
        )

        return peer_options_web_rtc_subscribe_options
