from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MoqAccess")


@_attrs_define
class MoqAccess:
    """Connection details for a MoQ relay client

    Attributes:
        connection_url (str): Relay connection URL with the JWT embedded as a `?jwt=` query parameter. Pass directly to
            a MoQ client SDK. Example: https://relay.fishjam.io/abc123?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9....
        token (str): JWT authorizing the MoQ relay connection, also embedded in `connection_url` Example: eyJhbGciOiJIUz
            I1NiIsInR5cCI6IkpXVCJ9.eyJyb290IjoiZmlzaGphbSIsInB1dCI6WyJteS1zdHJlYW0iXSwiZ2V0IjpbXSwiaWF0IjoxNzEzMzYwMDAwLCJle
            HAiOjE3MTMzNjM2MDB9.abc123.
    """

    connection_url: str
    token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_url = self.connection_url

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "connection_url": connection_url,
            "token": token,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_url = d.pop("connection_url")

        token = d.pop("token")

        moq_access = cls(
            connection_url=connection_url,
            token=token,
        )

        moq_access.additional_properties = d
        return moq_access

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
