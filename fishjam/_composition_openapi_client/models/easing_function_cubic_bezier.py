from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.easing_function_cubic_bezier_function_name import (
    EasingFunctionCubicBezierFunctionName,
)

T = TypeVar("T", bound="EasingFunctionCubicBezier")


@_attrs_define
class EasingFunctionCubicBezier:
    """
    Attributes:
        points (list[float]):
        function_name (EasingFunctionCubicBezierFunctionName):
    """

    points: list[float]
    function_name: EasingFunctionCubicBezierFunctionName
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points = self.points

        function_name = self.function_name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "points": points,
            "function_name": function_name,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        points = cast(list[float], d.pop("points"))

        function_name = EasingFunctionCubicBezierFunctionName(d.pop("function_name"))

        easing_function_cubic_bezier = cls(
            points=points,
            function_name=function_name,
        )

        easing_function_cubic_bezier.additional_properties = d
        return easing_function_cubic_bezier

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
