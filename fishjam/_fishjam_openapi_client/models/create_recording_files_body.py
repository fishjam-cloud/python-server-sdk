from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

if TYPE_CHECKING:
    from ..models.recording_config import RecordingConfig


T = TypeVar("T", bound="CreateRecordingFilesBody")


@_attrs_define
class CreateRecordingFilesBody:
    """
    Attributes:
        config (RecordingConfig): Recording configuration
        template (File): The React template bundle to render, at most 1 MiB
    """

    config: RecordingConfig
    template: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        template = self.template.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "config": config,
            "template": template,
        })

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append((
            "config",
            (None, json.dumps(self.config.to_dict()).encode(), "application/json"),
        ))

        files.append(("template", self.template.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recording_config import RecordingConfig

        d = dict(src_dict)
        config = RecordingConfig.from_dict(d.pop("config"))

        template = File(payload=BytesIO(d.pop("template")))

        create_recording_files_body = cls(
            config=config,
            template=template,
        )

        create_recording_files_body.additional_properties = d
        return create_recording_files_body

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
