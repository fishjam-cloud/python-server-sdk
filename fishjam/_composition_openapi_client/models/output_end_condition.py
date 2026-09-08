from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputEndCondition")


@_attrs_define
class OutputEndCondition:
    """This type defines when end of an input stream should trigger end of the output stream. Only one of those fields can
    be set at the time.
    Unless specified otherwise the input stream is considered finished/ended when:
    - TCP connection was dropped/closed.
    - RTCP Goodbye packet (`BYE`) was received.
    - Mp4 track has ended.
    - Input was unregistered already (or never registered).

        Attributes:
            any_of (list[str] | None | Unset): Terminate output stream if any of the input streams from the list are
                finished.
            all_of (list[str] | None | Unset): Terminate output stream if all the input streams from the list are finished.
            any_input (bool | None | Unset): Terminate output stream if any of the input streams ends. This includes streams
                added after the output was registered. In particular, output stream will **not be** terminated if no inputs were
                ever connected.
            all_inputs (bool | None | Unset): Terminate output stream if all the input streams finish. In particular, output
                stream will **be** terminated if no inputs were ever connected.
    """

    any_of: list[str] | None | Unset = UNSET
    all_of: list[str] | None | Unset = UNSET
    any_input: bool | None | Unset = UNSET
    all_inputs: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        any_of: list[str] | None | Unset
        if isinstance(self.any_of, Unset):
            any_of = UNSET
        elif isinstance(self.any_of, list):
            any_of = self.any_of

        else:
            any_of = self.any_of

        all_of: list[str] | None | Unset
        if isinstance(self.all_of, Unset):
            all_of = UNSET
        elif isinstance(self.all_of, list):
            all_of = self.all_of

        else:
            all_of = self.all_of

        any_input: bool | None | Unset
        if isinstance(self.any_input, Unset):
            any_input = UNSET
        else:
            any_input = self.any_input

        all_inputs: bool | None | Unset
        if isinstance(self.all_inputs, Unset):
            all_inputs = UNSET
        else:
            all_inputs = self.all_inputs

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if any_of is not UNSET:
            field_dict["any_of"] = any_of
        if all_of is not UNSET:
            field_dict["all_of"] = all_of
        if any_input is not UNSET:
            field_dict["any_input"] = any_input
        if all_inputs is not UNSET:
            field_dict["all_inputs"] = all_inputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_any_of(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                any_of_type_0 = cast(list[str], data)

                return any_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        any_of = _parse_any_of(d.pop("any_of", UNSET))

        def _parse_all_of(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                all_of_type_0 = cast(list[str], data)

                return all_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        all_of = _parse_all_of(d.pop("all_of", UNSET))

        def _parse_any_input(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        any_input = _parse_any_input(d.pop("any_input", UNSET))

        def _parse_all_inputs(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        all_inputs = _parse_all_inputs(d.pop("all_inputs", UNSET))

        output_end_condition = cls(
            any_of=any_of,
            all_of=all_of,
            any_input=any_input,
            all_inputs=all_inputs,
        )

        return output_end_condition
