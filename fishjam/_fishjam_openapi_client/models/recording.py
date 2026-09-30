from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recording_status import RecordingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.composition_source import CompositionSource
    from ..models.recording_file import RecordingFile
    from ..models.recording_metadata_type_0 import RecordingMetadataType0
    from ..models.template_source import TemplateSource


T = TypeVar("T", bound="Recording")


@_attrs_define
class Recording:
    """A recording and its current lifecycle status

    Attributes:
        files (list[RecordingFile]): Media files of the recording, in playback order. Empty until the recording is
            `available`.
        id (str): Assigned recording id
        source (CompositionSource | TemplateSource): The source for the recording
        status (RecordingStatus): Lifecycle status of a recording
        metadata (None | RecordingMetadataType0 | Unset): Free-form, user-supplied metadata used to organize and filter
            recordings
    """

    files: list[RecordingFile]
    id: str
    source: CompositionSource | TemplateSource
    status: RecordingStatus
    metadata: None | RecordingMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.composition_source import CompositionSource
        from ..models.recording_metadata_type_0 import RecordingMetadataType0

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        id = self.id

        source: dict[str, Any]
        if isinstance(self.source, CompositionSource):
            source = self.source.to_dict()
        else:
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
            "files": files,
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
        from ..models.recording_file import RecordingFile
        from ..models.recording_metadata_type_0 import RecordingMetadataType0
        from ..models.template_source import TemplateSource

        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = RecordingFile.from_dict(files_item_data)

            files.append(files_item)

        id = d.pop("id")

        def _parse_source(data: object) -> CompositionSource | TemplateSource:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_recording_source_type_0 = CompositionSource.from_dict(
                    data
                )

                return componentsschemas_recording_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_recording_source_type_1 = TemplateSource.from_dict(data)

            return componentsschemas_recording_source_type_1

        source = _parse_source(d.pop("source"))

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
            files=files,
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
