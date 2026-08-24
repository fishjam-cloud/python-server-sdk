from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.mp_4_input_type import Mp4InputType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Mp4Input")


@_attrs_define
class Mp4Input:
    """Input stream from an MP4 file.

    Attributes:
        url (str): URL of the MP4 file.
        type_ (Mp4InputType):
        loop (bool | None | Unset): (**default=`false`**) If input should be played in the loop. <span class="badge
            badge--primary">Added in v0.4.0</span>
    """

    url: str
    type_: Mp4InputType
    loop: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        type_ = self.type_.value

        loop: bool | None | Unset
        if isinstance(self.loop, Unset):
            loop = UNSET
        else:
            loop = self.loop

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "url": url,
            "type": type_,
        })
        if loop is not UNSET:
            field_dict["loop"] = loop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        type_ = Mp4InputType(d.pop("type"))

        def _parse_loop(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        loop = _parse_loop(d.pop("loop", UNSET))

        mp_4_input = cls(
            url=url,
            type_=type_,
            loop=loop,
        )

        return mp_4_input
