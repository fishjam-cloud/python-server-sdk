from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MoqToken")


@_attrs_define
class MoqToken:
    """Token for authorizing a MoQ relay connection

    Attributes:
        token (str): JWT token for MoQ relay Example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb290IjoiZmlzaGphbSIsInB1d
            CI6WyJteS1zdHJlYW0iXSwiZ2V0IjpbXSwiaWF0IjoxNzEzMzYwMDAwLCJleHAiOjE3MTMzNjM2MDB9.abc123.
    """

    token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "token": token,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        moq_token = cls(
            token=token,
        )

        moq_token.additional_properties = d
        return moq_token

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
