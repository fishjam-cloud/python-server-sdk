from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.room_type import RoomType
from ..models.video_codec import VideoCodec
from ..types import UNSET, Unset

T = TypeVar("T", bound="RoomConfig")


@_attrs_define
class RoomConfig:
    """Room configuration

    Attributes:
        max_peers (int | None | Unset): Maximum amount of peers allowed into the room Example: 10.
        public (bool | Unset): True if livestream viewers can omit specifying a token. Default: False.
        room_type (RoomType | Unset): The use-case of the room. If not provided, this defaults to conference.
        video_codec (VideoCodec | Unset): Enforces video codec for each peer in the room
        webhook_url (None | str | Unset): URL where Fishjam notifications will be sent Example:
            https://backend.address.com/fishjam-notifications-endpoint.
    """

    max_peers: int | None | Unset = UNSET
    public: bool | Unset = False
    room_type: RoomType | Unset = UNSET
    video_codec: VideoCodec | Unset = UNSET
    webhook_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_peers: int | None | Unset
        if isinstance(self.max_peers, Unset):
            max_peers = UNSET
        else:
            max_peers = self.max_peers

        public = self.public

        room_type: str | Unset = UNSET
        if not isinstance(self.room_type, Unset):
            room_type = self.room_type.value

        video_codec: str | Unset = UNSET
        if not isinstance(self.video_codec, Unset):
            video_codec = self.video_codec.value

        webhook_url: None | str | Unset
        if isinstance(self.webhook_url, Unset):
            webhook_url = UNSET
        else:
            webhook_url = self.webhook_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_peers is not UNSET:
            field_dict["maxPeers"] = max_peers
        if public is not UNSET:
            field_dict["public"] = public
        if room_type is not UNSET:
            field_dict["roomType"] = room_type
        if video_codec is not UNSET:
            field_dict["videoCodec"] = video_codec
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_max_peers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_peers = _parse_max_peers(d.pop("maxPeers", UNSET))

        public = d.pop("public", UNSET)

        _room_type = d.pop("roomType", UNSET)
        room_type: RoomType | Unset
        if isinstance(_room_type, Unset):
            room_type = UNSET
        else:
            room_type = RoomType(_room_type)

        _video_codec = d.pop("videoCodec", UNSET)
        video_codec: VideoCodec | Unset
        if isinstance(_video_codec, Unset):
            video_codec = UNSET
        else:
            video_codec = VideoCodec(_video_codec)

        def _parse_webhook_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        webhook_url = _parse_webhook_url(d.pop("webhookUrl", UNSET))

        room_config = cls(
            max_peers=max_peers,
            public=public,
            room_type=room_type,
            video_codec=video_codec,
            webhook_url=webhook_url,
        )

        return room_config
