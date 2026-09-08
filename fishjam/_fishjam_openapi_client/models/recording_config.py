from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.composition_source import CompositionSource
    from ..models.recording_config_metadata_type_0 import RecordingConfigMetadataType0


T = TypeVar("T", bound="RecordingConfig")


@_attrs_define
class RecordingConfig:
    """Recording configuration

    Attributes:
        source (CompositionSource): Recording source coming from composition
        metadata (None | RecordingConfigMetadataType0 | Unset): Free-form, user-supplied metadata used to organize and
            filter recordings
    """

    source: CompositionSource
    metadata: None | RecordingConfigMetadataType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.recording_config_metadata_type_0 import (
            RecordingConfigMetadataType0,
        )

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

        d = dict(src_dict)
        source = CompositionSource.from_dict(d.pop("source"))

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
