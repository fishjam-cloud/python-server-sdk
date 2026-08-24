from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.easing_function_bounce_function_name import (
    EasingFunctionBounceFunctionName,
)

T = TypeVar("T", bound="EasingFunctionBounce")


@_attrs_define
class EasingFunctionBounce:
    """
    Attributes:
        function_name (EasingFunctionBounceFunctionName):
    """

    function_name: EasingFunctionBounceFunctionName
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function_name = self.function_name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "function_name": function_name,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        function_name = EasingFunctionBounceFunctionName(d.pop("function_name"))

        easing_function_bounce = cls(
            function_name=function_name,
        )

        easing_function_bounce.additional_properties = d
        return easing_function_bounce

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
