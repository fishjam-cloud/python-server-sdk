from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.track_forwarding_info import TrackForwardingInfo


T = TypeVar("T", bound="CompositionInfo")


@_attrs_define
class CompositionInfo:
    """Composition and track forwarding state for the room

    Attributes:
        composition_url (str): URL of the active composition Example: https://rtc.fishjam.io/api/composition/12asdfxcf.
        forwardings (list['TrackForwardingInfo']): List of active track forwardings
    """

    composition_url: str
    forwardings: list["TrackForwardingInfo"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        composition_url = self.composition_url

        forwardings = []
        for forwardings_item_data in self.forwardings:
            forwardings_item = forwardings_item_data.to_dict()
            forwardings.append(forwardings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "compositionUrl": composition_url,
            "forwardings": forwardings,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.track_forwarding_info import TrackForwardingInfo

        d = dict(src_dict)
        composition_url = d.pop("compositionUrl")

        forwardings = []
        _forwardings = d.pop("forwardings")
        for forwardings_item_data in _forwardings:
            forwardings_item = TrackForwardingInfo.from_dict(forwardings_item_data)

            forwardings.append(forwardings_item)

        composition_info = cls(
            composition_url=composition_url,
            forwardings=forwardings,
        )

        composition_info.additional_properties = d
        return composition_info

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
