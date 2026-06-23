from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoqAccessConfig")


@_attrs_define
class MoqAccessConfig:
    """MoQ access configuration

    Attributes:
        publish_path (None | str | Unset): Path under the root the token grants publish access to Example: my-stream.
        subscribe_path (None | str | Unset): Path under the root the token grants subscribe access to Example: my-
            stream.
    """

    publish_path: None | str | Unset = UNSET
    subscribe_path: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        publish_path: None | str | Unset
        if isinstance(self.publish_path, Unset):
            publish_path = UNSET
        else:
            publish_path = self.publish_path

        subscribe_path: None | str | Unset
        if isinstance(self.subscribe_path, Unset):
            subscribe_path = UNSET
        else:
            subscribe_path = self.subscribe_path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if publish_path is not UNSET:
            field_dict["publishPath"] = publish_path
        if subscribe_path is not UNSET:
            field_dict["subscribePath"] = subscribe_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_publish_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publish_path = _parse_publish_path(d.pop("publishPath", UNSET))

        def _parse_subscribe_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscribe_path = _parse_subscribe_path(d.pop("subscribePath", UNSET))

        moq_access_config = cls(
            publish_path=publish_path,
            subscribe_path=subscribe_path,
        )

        return moq_access_config
