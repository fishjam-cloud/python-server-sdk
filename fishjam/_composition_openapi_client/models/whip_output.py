from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.whip_output_type import WhipOutputType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_whip_audio_options import OutputWhipAudioOptions
    from ..models.output_whip_video_options import OutputWhipVideoOptions


T = TypeVar("T", bound="WhipOutput")


@_attrs_define
class WhipOutput:
    """
    Attributes:
        endpoint_url (str): WHIP server endpoint
        type_ (WhipOutputType):
        bearer_token (None | str | Unset):
        video (None | OutputWhipVideoOptions | Unset):
        audio (None | OutputWhipAudioOptions | Unset):
    """

    endpoint_url: str
    type_: WhipOutputType
    bearer_token: None | str | Unset = UNSET
    video: None | OutputWhipVideoOptions | Unset = UNSET
    audio: None | OutputWhipAudioOptions | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.output_whip_audio_options import OutputWhipAudioOptions
        from ..models.output_whip_video_options import OutputWhipVideoOptions

        endpoint_url = self.endpoint_url

        type_ = self.type_.value

        bearer_token: None | str | Unset
        if isinstance(self.bearer_token, Unset):
            bearer_token = UNSET
        else:
            bearer_token = self.bearer_token

        video: dict[str, Any] | None | Unset
        if isinstance(self.video, Unset):
            video = UNSET
        elif isinstance(self.video, OutputWhipVideoOptions):
            video = self.video.to_dict()
        else:
            video = self.video

        audio: dict[str, Any] | None | Unset
        if isinstance(self.audio, Unset):
            audio = UNSET
        elif isinstance(self.audio, OutputWhipAudioOptions):
            audio = self.audio.to_dict()
        else:
            audio = self.audio

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "endpoint_url": endpoint_url,
            "type": type_,
        })
        if bearer_token is not UNSET:
            field_dict["bearer_token"] = bearer_token
        if video is not UNSET:
            field_dict["video"] = video
        if audio is not UNSET:
            field_dict["audio"] = audio

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_whip_audio_options import OutputWhipAudioOptions
        from ..models.output_whip_video_options import OutputWhipVideoOptions

        d = dict(src_dict)
        endpoint_url = d.pop("endpoint_url")

        type_ = WhipOutputType(d.pop("type"))

        def _parse_bearer_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bearer_token = _parse_bearer_token(d.pop("bearer_token", UNSET))

        def _parse_video(data: object) -> None | OutputWhipVideoOptions | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_type_1 = OutputWhipVideoOptions.from_dict(data)

                return video_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OutputWhipVideoOptions | Unset, data)

        video = _parse_video(d.pop("video", UNSET))

        def _parse_audio(data: object) -> None | OutputWhipAudioOptions | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                audio_type_1 = OutputWhipAudioOptions.from_dict(data)

                return audio_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OutputWhipAudioOptions | Unset, data)

        audio = _parse_audio(d.pop("audio", UNSET))

        whip_output = cls(
            endpoint_url=endpoint_url,
            type_=type_,
            bearer_token=bearer_token,
            video=video,
            audio=audio,
        )

        return whip_output
