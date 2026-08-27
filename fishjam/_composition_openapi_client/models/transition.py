from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.easing_function_bounce import EasingFunctionBounce
    from ..models.easing_function_cubic_bezier import EasingFunctionCubicBezier
    from ..models.easing_function_linear import EasingFunctionLinear


T = TypeVar("T", bound="Transition")


@_attrs_define
class Transition:
    """
    Attributes:
        duration_ms (float): Duration of a transition in milliseconds.
        easing_function (EasingFunctionBounce | EasingFunctionCubicBezier | EasingFunctionLinear | None | Unset):
        should_interrupt (bool | None | Unset): (**default=`false`**) On scene update, if there is already a transition
            in progress,
            it will be interrupted and the new transition will start from the current state.
    """

    duration_ms: float
    easing_function: (
        EasingFunctionBounce
        | EasingFunctionCubicBezier
        | EasingFunctionLinear
        | None
        | Unset
    ) = UNSET
    should_interrupt: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.easing_function_bounce import EasingFunctionBounce
        from ..models.easing_function_cubic_bezier import EasingFunctionCubicBezier
        from ..models.easing_function_linear import EasingFunctionLinear

        duration_ms = self.duration_ms

        easing_function: dict[str, Any] | None | Unset
        if isinstance(self.easing_function, Unset):
            easing_function = UNSET
        elif isinstance(self.easing_function, EasingFunctionLinear):
            easing_function = self.easing_function.to_dict()
        elif isinstance(self.easing_function, EasingFunctionBounce):
            easing_function = self.easing_function.to_dict()
        elif isinstance(self.easing_function, EasingFunctionCubicBezier):
            easing_function = self.easing_function.to_dict()
        else:
            easing_function = self.easing_function

        should_interrupt: bool | None | Unset
        if isinstance(self.should_interrupt, Unset):
            should_interrupt = UNSET
        else:
            should_interrupt = self.should_interrupt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "duration_ms": duration_ms,
        })
        if easing_function is not UNSET:
            field_dict["easing_function"] = easing_function
        if should_interrupt is not UNSET:
            field_dict["should_interrupt"] = should_interrupt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.easing_function_bounce import EasingFunctionBounce
        from ..models.easing_function_cubic_bezier import EasingFunctionCubicBezier
        from ..models.easing_function_linear import EasingFunctionLinear

        d = dict(src_dict)
        duration_ms = d.pop("duration_ms")

        def _parse_easing_function(
            data: object,
        ) -> (
            EasingFunctionBounce
            | EasingFunctionCubicBezier
            | EasingFunctionLinear
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_easing_function_easing_function_linear = (
                    EasingFunctionLinear.from_dict(data)
                )

                return componentsschemas_easing_function_easing_function_linear
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_easing_function_easing_function_bounce = (
                    EasingFunctionBounce.from_dict(data)
                )

                return componentsschemas_easing_function_easing_function_bounce
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_easing_function_easing_function_cubic_bezier = (
                    EasingFunctionCubicBezier.from_dict(data)
                )

                return componentsschemas_easing_function_easing_function_cubic_bezier
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                EasingFunctionBounce
                | EasingFunctionCubicBezier
                | EasingFunctionLinear
                | None
                | Unset,
                data,
            )

        easing_function = _parse_easing_function(d.pop("easing_function", UNSET))

        def _parse_should_interrupt(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        should_interrupt = _parse_should_interrupt(d.pop("should_interrupt", UNSET))

        transition = cls(
            duration_ms=duration_ms,
            easing_function=easing_function,
            should_interrupt=should_interrupt,
        )

        transition.additional_properties = d
        return transition

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
