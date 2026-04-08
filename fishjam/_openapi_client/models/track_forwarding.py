from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackForwarding")


@_attrs_define
class TrackForwarding:
    """Track forwardings for a room

    Attributes:
        composition_url (str): URL for the composition
        selector (Union[Unset, str]): Selects tracks that should be forwarded, currently only "all" is supported
            Default: 'all'.
    """

    composition_url: str
    selector: Union[Unset, str] = "all"

    def to_dict(self) -> dict[str, Any]:
        composition_url = self.composition_url

        selector = self.selector

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "compositionURL": composition_url,
        })
        if selector is not UNSET:
            field_dict["selector"] = selector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        composition_url = d.pop("compositionURL")

        selector = d.pop("selector", UNSET)

        track_forwarding = cls(
            composition_url=composition_url,
            selector=selector,
        )

        return track_forwarding
