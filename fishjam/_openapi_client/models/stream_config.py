from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StreamConfig")


@_attrs_define
class StreamConfig:
    """Stream configuration

    Attributes:
        audio_only (Union[None, Unset, bool]): Restrics stream to audio only Default: False.
        public (Union[Unset, bool]): True if livestream viewers can omit specifying a token. Default: False.
        webhook_url (Union[None, Unset, str]): Webhook URL for receiving server notifications
    """

    audio_only: Union[None, Unset, bool] = False
    public: Union[Unset, bool] = False
    webhook_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        audio_only: Union[None, Unset, bool]
        if isinstance(self.audio_only, Unset):
            audio_only = UNSET
        else:
            audio_only = self.audio_only

        public = self.public

        webhook_url: Union[None, Unset, str]
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

        def _parse_audio_only(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        audio_only = _parse_audio_only(d.pop("audioOnly", UNSET))

        public = d.pop("public", UNSET)

        def _parse_webhook_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        webhook_url = _parse_webhook_url(d.pop("webhookUrl", UNSET))

        stream_config = cls(
            audio_only=audio_only,
            public=public,
            webhook_url=webhook_url,
        )

        return stream_config
