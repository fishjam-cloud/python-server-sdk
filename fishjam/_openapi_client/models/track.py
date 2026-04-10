from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.track_type import TrackType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.track_metadata import TrackMetadata


T = TypeVar("T", bound="Track")


@_attrs_define
class Track:
    """Describes media track of a Peer

    Attributes:
        id (str | Unset): Assigned track id Example: 8dbd2e6b-a1e7-4670-95a2-0262aa6c6321.
        metadata (None | TrackMetadata | Unset):  Example: {'source': 'camera'}.
        type_ (TrackType | Unset):
    """

    id: str | Unset = UNSET
    metadata: None | TrackMetadata | Unset = UNSET
    type_: TrackType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.track_metadata import TrackMetadata

        id = self.id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, TrackMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.track_metadata import TrackMetadata

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_metadata(data: object) -> None | TrackMetadata | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_track_metadata_type_0 = TrackMetadata.from_dict(data)

                return componentsschemas_track_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TrackMetadata | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: TrackType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TrackType(_type_)

        track = cls(
            id=id,
            metadata=metadata,
            type_=type_,
        )

        track.additional_properties = d
        return track

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
