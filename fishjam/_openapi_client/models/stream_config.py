from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StreamConfig")


@_attrs_define
class StreamConfig:
    """Stream configuration

    Attributes:
        audio_only (bool | None | Unset): Restrics stream to audio only Default: False.
        public (bool | Unset): True if livestream viewers can omit specifying a token. Default: False.
        webhook_url (None | str | Unset): Webhook URL for receiving server notifications
    """

    audio_only: bool | None | Unset = False
    public: bool | Unset = False
    webhook_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        audio_only: bool | None | Unset
        if isinstance(self.audio_only, Unset):
            audio_only = UNSET
        else:
            audio_only = self.audio_only

        public = self.public

        webhook_url: None | str | Unset
        if isinstance(self.webhook_url, Unset):
            webhook_url = UNSET
        else:
            webhook_url = self.webhook_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if audio_only is not UNSET:
            field_dict["audioOnly"] = audio_only
        if public is not UNSET:
            field_dict["public"] = public
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_audio_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        audio_only = _parse_audio_only(d.pop("audioOnly", UNSET))

        public = d.pop("public", UNSET)

        def _parse_webhook_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        webhook_url = _parse_webhook_url(d.pop("webhookUrl", UNSET))

        stream_config = cls(
            audio_only=audio_only,
            public=public,
            webhook_url=webhook_url,
        )

        return stream_config
