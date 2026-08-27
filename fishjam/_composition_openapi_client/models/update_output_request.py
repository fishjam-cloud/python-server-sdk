from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audio_scene import AudioScene
    from ..models.video_scene import VideoScene


T = TypeVar("T", bound="UpdateOutputRequest")


@_attrs_define
class UpdateOutputRequest:
    """
    Attributes:
        video (None | Unset | VideoScene):
        audio (AudioScene | None | Unset):
        schedule_time_ms (float | None | Unset):
    """

    video: None | Unset | VideoScene = UNSET
    audio: AudioScene | None | Unset = UNSET
    schedule_time_ms: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.audio_scene import AudioScene
        from ..models.video_scene import VideoScene

        video: dict[str, Any] | None | Unset
        if isinstance(self.video, Unset):
            video = UNSET
        elif isinstance(self.video, VideoScene):
            video = self.video.to_dict()
        else:
            video = self.video

        audio: dict[str, Any] | None | Unset
        if isinstance(self.audio, Unset):
            audio = UNSET
        elif isinstance(self.audio, AudioScene):
            audio = self.audio.to_dict()
        else:
            audio = self.audio

        schedule_time_ms: float | None | Unset
        if isinstance(self.schedule_time_ms, Unset):
            schedule_time_ms = UNSET
        else:
            schedule_time_ms = self.schedule_time_ms

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if video is not UNSET:
            field_dict["video"] = video
        if audio is not UNSET:
            field_dict["audio"] = audio
        if schedule_time_ms is not UNSET:
            field_dict["schedule_time_ms"] = schedule_time_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audio_scene import AudioScene
        from ..models.video_scene import VideoScene

        d = dict(src_dict)

        def _parse_video(data: object) -> None | Unset | VideoScene:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_type_1 = VideoScene.from_dict(data)

                return video_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VideoScene, data)

        video = _parse_video(d.pop("video", UNSET))

        def _parse_audio(data: object) -> AudioScene | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                audio_type_1 = AudioScene.from_dict(data)

                return audio_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AudioScene | None | Unset, data)

        audio = _parse_audio(d.pop("audio", UNSET))

        def _parse_schedule_time_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        schedule_time_ms = _parse_schedule_time_ms(d.pop("schedule_time_ms", UNSET))

        update_output_request = cls(
            video=video,
            audio=audio,
            schedule_time_ms=schedule_time_ms,
        )

        return update_output_request
