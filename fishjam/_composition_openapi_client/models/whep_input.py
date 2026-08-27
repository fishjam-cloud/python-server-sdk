from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.whep_input_type import WhepInputType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WhepInput")


@_attrs_define
class WhepInput:
    """
    Attributes:
        endpoint_url (str): WHEP server endpoint URL
        type_ (WhepInputType):
        bearer_token (None | str | Unset): Optional Bearer token for auth
        video (bool | None | Unset): If `true`, requests a h264-encoded video track.
            If not provided, it defaults to `true`
    """

    endpoint_url: str
    type_: WhepInputType
    bearer_token: None | str | Unset = UNSET
    video: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        endpoint_url = self.endpoint_url

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
            "endpoint_url": endpoint_url,
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
        endpoint_url = d.pop("endpoint_url")

        type_ = WhepInputType(d.pop("type"))

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

        whep_input = cls(
            endpoint_url=endpoint_url,
            type_=type_,
            bearer_token=bearer_token,
            video=video,
        )

        return whep_input
