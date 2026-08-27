from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_end_condition import OutputEndCondition
    from ..models.resolution import Resolution
    from ..models.video_scene import VideoScene


T = TypeVar("T", bound="OutputWhipVideoOptions")


@_attrs_define
class OutputWhipVideoOptions:
    """
    Attributes:
        resolution (Resolution):
        initial (VideoScene):
        send_eos_when (None | OutputEndCondition | Unset):
    """

    resolution: Resolution
    initial: VideoScene
    send_eos_when: None | OutputEndCondition | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.output_end_condition import OutputEndCondition

        resolution = self.resolution.to_dict()

        initial = self.initial.to_dict()

        send_eos_when: dict[str, Any] | None | Unset
        if isinstance(self.send_eos_when, Unset):
            send_eos_when = UNSET
        elif isinstance(self.send_eos_when, OutputEndCondition):
            send_eos_when = self.send_eos_when.to_dict()
        else:
            send_eos_when = self.send_eos_when

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "resolution": resolution,
            "initial": initial,
        })
        if send_eos_when is not UNSET:
            field_dict["send_eos_when"] = send_eos_when

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_end_condition import OutputEndCondition
        from ..models.resolution import Resolution
        from ..models.video_scene import VideoScene

        d = dict(src_dict)
        resolution = Resolution.from_dict(d.pop("resolution"))

        initial = VideoScene.from_dict(d.pop("initial"))

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

        output_whip_video_options = cls(
            resolution=resolution,
            initial=initial,
            send_eos_when=send_eos_when,
        )

        return output_whip_video_options
