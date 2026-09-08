from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.whip_input_type import WhipInputType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WhipInput")


@_attrs_define
class WhipInput:
    """
    Attributes:
        type_ (WhipInputType):
        bearer_token (None | str | Unset): Token used for authentication in WHIP protocol. If not provided, the random
            value
            will be generated and returned in the response.
        video (bool | None | Unset): If `true`, accepts a h264-encoded video track.
            If not provided, it defaults to `true`
    """

    type_: WhipInputType
    bearer_token: None | str | Unset = UNSET
    video: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        bearer_token: None | str | Unset
        if isinstance(self.bearer_token, Unset):
            bearer_token = UNSET
        else:
            bearer_token = self.bearer_token

        video: bool | None | Unset
        if isinstance(self.video, Unset):
            video = UNSET
        else:
            video = self.video

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if bearer_token is not UNSET:
            field_dict["bearer_token"] = bearer_token
        if video is not UNSET:
            field_dict["video"] = video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = WhipInputType(d.pop("type"))

        def _parse_bearer_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bearer_token = _parse_bearer_token(d.pop("bearer_token", UNSET))

        def _parse_video(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        video = _parse_video(d.pop("video", UNSET))

        whip_input = cls(
            type_=type_,
            bearer_token=bearer_token,
            video=video,
        )

        return whip_input
