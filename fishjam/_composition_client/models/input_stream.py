from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.input_stream_type import InputStreamType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InputStream")


@_attrs_define
class InputStream:
    """
    Attributes:
        input_id (str):
        type_ (InputStreamType):
        id (None | str | Unset):
    """

    input_id: str
    type_: InputStreamType
    id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        input_id = self.input_id

        type_ = self.type_.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "input_id": input_id,
            "type": type_,
        })
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_id = d.pop("input_id")

        type_ = InputStreamType(d.pop("type"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        input_stream = cls(
            input_id=input_id,
            type_=type_,
            id=id,
        )

        return input_stream
