from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recording_status import RecordingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.composition_source import CompositionSource
    from ..models.recording_metadata_type_0 import RecordingMetadataType0


T = TypeVar("T", bound="Recording")


@_attrs_define
class Recording:
    """A recording and its current lifecycle status

    Attributes:
        id (str): Assigned recording id
        source (CompositionSource): Recording source coming from composition
        status (RecordingStatus): Lifecycle status of a recording
        metadata (None | RecordingMetadataType0 | Unset): Free-form, user-supplied metadata used to organize and filter
            recordings
    """

    id: str
    source: CompositionSource
    status: RecordingStatus
    metadata: None | RecordingMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.recording_metadata_type_0 import RecordingMetadataType0

        id = self.id

        source = self.source.to_dict()

        status = self.status.value

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, RecordingMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "source": source,
            "status": status,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.composition_source import CompositionSource
        from ..models.recording_metadata_type_0 import RecordingMetadataType0

        d = dict(src_dict)
        id = d.pop("id")

        source = CompositionSource.from_dict(d.pop("source"))

        status = RecordingStatus(d.pop("status"))

        def _parse_metadata(data: object) -> None | RecordingMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = RecordingMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecordingMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        recording = cls(
            id=id,
            source=source,
            status=status,
            metadata=metadata,
        )

        recording.additional_properties = d
        return recording

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
