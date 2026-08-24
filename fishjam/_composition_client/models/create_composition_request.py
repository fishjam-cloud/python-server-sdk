from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCompositionRequest")


@_attrs_define
class CreateCompositionRequest:
    """
    Attributes:
        autostart (bool | Unset): If true, outputs will immediately start producing audio and video.
            If false, call `POST /api/composition/{composition_id}/start` to start the composition. Default: True.
        cleanup_without_inputs (bool | Unset): If true (default), the composition will be cleaned up after 5 minutes
            when all **inputs**
            have zero bitrate, regardless of output bitrate. This prevents circular liveness when
            composition output is sent to a stream.
            If false, cleanup only triggers when both inputs and outputs have zero bitrate. Default: True.
    """

    autostart: bool | Unset = True
    cleanup_without_inputs: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        autostart = self.autostart

        cleanup_without_inputs = self.cleanup_without_inputs

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if autostart is not UNSET:
            field_dict["autostart"] = autostart
        if cleanup_without_inputs is not UNSET:
            field_dict["cleanup_without_inputs"] = cleanup_without_inputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        autostart = d.pop("autostart", UNSET)

        cleanup_without_inputs = d.pop("cleanup_without_inputs", UNSET)

        create_composition_request = cls(
            autostart=autostart,
            cleanup_without_inputs=cleanup_without_inputs,
        )

        return create_composition_request
