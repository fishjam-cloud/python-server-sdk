from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.rtmp_input_type import RtmpInputType

T = TypeVar("T", bound="RtmpInput")


@_attrs_define
class RtmpInput:
    """
    Attributes:
        stream_key (str): The RTMP stream key.
            This is the path segment of the RTMP stream URL that Smelter listens on for incoming streams.
            Format: `rtmp://<ip_address>:<port>/<stream_key>`
        type_ (RtmpInputType):
    """

    stream_key: str
    type_: RtmpInputType

    def to_dict(self) -> dict[str, Any]:
        stream_key = self.stream_key

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "stream_key": stream_key,
            "type": type_,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stream_key = d.pop("stream_key")

        type_ = RtmpInputType(d.pop("type"))

        rtmp_input = cls(
            stream_key=stream_key,
            type_=type_,
        )

        return rtmp_input
