from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.composition_source import CompositionSource
    from ..models.recording_config_metadata_type_0 import RecordingConfigMetadataType0
    from ..models.template_source import TemplateSource


T = TypeVar("T", bound="RecordingConfig")


@_attrs_define
class RecordingConfig:
    """Recording configuration

    Attributes:
        source (CompositionSource | TemplateSource): The source for the recording
        metadata (None | RecordingConfigMetadataType0 | Unset): Free-form, user-supplied metadata used to organize and
            filter recordings
    """

    source: CompositionSource | TemplateSource
    metadata: None | RecordingConfigMetadataType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.composition_source import CompositionSource
        from ..models.recording_config_metadata_type_0 import (
            RecordingConfigMetadataType0,
        )

        source: dict[str, Any]
        if isinstance(self.source, CompositionSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, RecordingConfigMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "source": source,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.composition_source import CompositionSource
        from ..models.recording_config_metadata_type_0 import (
            RecordingConfigMetadataType0,
        )
        from ..models.template_source import TemplateSource

        d = dict(src_dict)

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

        def _parse_metadata(
            data: object,
        ) -> None | RecordingConfigMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = RecordingConfigMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecordingConfigMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        recording_config = cls(
            source=source,
            metadata=metadata,
        )

        return recording_config
