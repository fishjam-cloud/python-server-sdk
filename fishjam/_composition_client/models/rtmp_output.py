from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.rtmp_output_type import RtmpOutputType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_rtmp_client_audio_options import OutputRtmpClientAudioOptions
    from ..models.output_rtmp_client_video_options import OutputRtmpClientVideoOptions


T = TypeVar("T", bound="RtmpOutput")


@_attrs_define
class RtmpOutput:
    """
    Attributes:
        url (str): RTMP endpoint url.
        type_ (RtmpOutputType):
        video (None | OutputRtmpClientVideoOptions | Unset):
        audio (None | OutputRtmpClientAudioOptions | Unset):
    """

    url: str
    type_: RtmpOutputType
    video: None | OutputRtmpClientVideoOptions | Unset = UNSET
    audio: None | OutputRtmpClientAudioOptions | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.output_rtmp_client_audio_options import (
            OutputRtmpClientAudioOptions,
        )
        from ..models.output_rtmp_client_video_options import (
            OutputRtmpClientVideoOptions,
        )

        url = self.url

        type_ = self.type_.value

        video: dict[str, Any] | None | Unset
        if isinstance(self.video, Unset):
            video = UNSET
        elif isinstance(self.video, OutputRtmpClientVideoOptions):
            video = self.video.to_dict()
        else:
            video = self.video

        audio: dict[str, Any] | None | Unset
        if isinstance(self.audio, Unset):
            audio = UNSET
        elif isinstance(self.audio, OutputRtmpClientAudioOptions):
            audio = self.audio.to_dict()
        else:
            audio = self.audio

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "url": url,
            "type": type_,
        })
        if video is not UNSET:
            field_dict["video"] = video
        if audio is not UNSET:
            field_dict["audio"] = audio

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_rtmp_client_audio_options import (
            OutputRtmpClientAudioOptions,
        )
        from ..models.output_rtmp_client_video_options import (
            OutputRtmpClientVideoOptions,
        )

        d = dict(src_dict)
        url = d.pop("url")

        type_ = RtmpOutputType(d.pop("type"))

        def _parse_video(data: object) -> None | OutputRtmpClientVideoOptions | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_type_1 = OutputRtmpClientVideoOptions.from_dict(data)

                return video_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OutputRtmpClientVideoOptions | Unset, data)

        video = _parse_video(d.pop("video", UNSET))

        def _parse_audio(data: object) -> None | OutputRtmpClientAudioOptions | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                audio_type_1 = OutputRtmpClientAudioOptions.from_dict(data)

                return audio_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OutputRtmpClientAudioOptions | Unset, data)

        audio = _parse_audio(d.pop("audio", UNSET))

        rtmp_output = cls(
            url=url,
            type_=type_,
            video=video,
            audio=audio,
        )

        return rtmp_output
