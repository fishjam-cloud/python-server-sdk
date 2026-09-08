from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

if TYPE_CHECKING:
    from ..models.rtmp_output import RtmpOutput
    from ..models.whip_output import WhipOutput


T = TypeVar("T", bound="RegisterTemplateOutput")


@_attrs_define
class RegisterTemplateOutput:
    """
    Attributes:
        config (RtmpOutput | WhipOutput):
        template (File):
    """

    config: RtmpOutput | WhipOutput
    template: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rtmp_output import RtmpOutput

        config: dict[str, Any]
        if isinstance(self.config, RtmpOutput):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        template = self.template.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "config": config,
            "template": template,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rtmp_output import RtmpOutput
        from ..models.whip_output import WhipOutput

        d = dict(src_dict)

        def _parse_config(data: object) -> RtmpOutput | WhipOutput:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_register_output_type_0 = RtmpOutput.from_dict(data)

                return componentsschemas_register_output_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_register_output_type_1 = WhipOutput.from_dict(data)

            return componentsschemas_register_output_type_1

        config = _parse_config(d.pop("config"))

        template = File(payload=BytesIO(d.pop("template")))

        register_template_output = cls(
            config=config,
            template=template,
        )

        register_template_output.additional_properties = d
        return register_template_output

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
