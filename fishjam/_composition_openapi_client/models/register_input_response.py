from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterInputResponse")


@_attrs_define
class RegisterInputResponse:
    """
    Attributes:
        bearer_token (None | str | Unset):
        endpoint_route (None | str | Unset):
        video_duration_ms (int | None | Unset):
        audio_duration_ms (int | None | Unset):
        publish_url (None | str | Unset):
    """

    bearer_token: None | str | Unset = UNSET
    endpoint_route: None | str | Unset = UNSET
    video_duration_ms: int | None | Unset = UNSET
    audio_duration_ms: int | None | Unset = UNSET
    publish_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bearer_token: None | str | Unset
        if isinstance(self.bearer_token, Unset):
            bearer_token = UNSET
        else:
            bearer_token = self.bearer_token

        endpoint_route: None | str | Unset
        if isinstance(self.endpoint_route, Unset):
            endpoint_route = UNSET
        else:
            endpoint_route = self.endpoint_route

        video_duration_ms: int | None | Unset
        if isinstance(self.video_duration_ms, Unset):
            video_duration_ms = UNSET
        else:
            video_duration_ms = self.video_duration_ms

        audio_duration_ms: int | None | Unset
        if isinstance(self.audio_duration_ms, Unset):
            audio_duration_ms = UNSET
        else:
            audio_duration_ms = self.audio_duration_ms

        publish_url: None | str | Unset
        if isinstance(self.publish_url, Unset):
            publish_url = UNSET
        else:
            publish_url = self.publish_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if bearer_token is not UNSET:
            field_dict["bearer_token"] = bearer_token
        if endpoint_route is not UNSET:
            field_dict["endpoint_route"] = endpoint_route
        if video_duration_ms is not UNSET:
            field_dict["video_duration_ms"] = video_duration_ms
        if audio_duration_ms is not UNSET:
            field_dict["audio_duration_ms"] = audio_duration_ms
        if publish_url is not UNSET:
            field_dict["publish_url"] = publish_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_bearer_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bearer_token = _parse_bearer_token(d.pop("bearer_token", UNSET))

        def _parse_endpoint_route(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        endpoint_route = _parse_endpoint_route(d.pop("endpoint_route", UNSET))

        def _parse_video_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        video_duration_ms = _parse_video_duration_ms(d.pop("video_duration_ms", UNSET))

        def _parse_audio_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        audio_duration_ms = _parse_audio_duration_ms(d.pop("audio_duration_ms", UNSET))

        def _parse_publish_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publish_url = _parse_publish_url(d.pop("publish_url", UNSET))

        register_input_response = cls(
            bearer_token=bearer_token,
            endpoint_route=endpoint_route,
            video_duration_ms=video_duration_ms,
            audio_duration_ms=audio_duration_ms,
            publish_url=publish_url,
        )

        return register_input_response
