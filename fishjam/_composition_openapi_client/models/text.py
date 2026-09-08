from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.horizontal_align import HorizontalAlign
from ..models.text_style import TextStyle
from ..models.text_type import TextType
from ..models.text_weight import TextWeight
from ..models.text_wrap_mode import TextWrapMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="Text")


@_attrs_define
class Text:
    """
    Attributes:
        text (str): Text that will be rendered.
        font_size (float): Font size in pixels.
        type_ (TextType):
        id (None | str | Unset):
        width (float | None | Unset): Width of a texture that text will be rendered on. If not provided, the resulting
            texture
            will be sized based on the defined text but limited to `max_width` value.
        height (float | None | Unset): Height of a texture that text will be rendered on. If not provided, the resulting
            texture
            will be sized based on the defined text but limited to `max_height` value.
            It's an error to provide `height` if `width` is not defined.
        max_width (float | None | Unset): (**default=`7682`**) Maximal `width`. Limits the width of the texture that the
            text will be rendered on.
            Value is ignored if `width` is defined.
        max_height (float | None | Unset): (**default=`4320`**) Maximal `height`. Limits the height of the texture that
            the text will be rendered on.
            Value is ignored if height is defined.
        line_height (float | None | Unset): Distance between lines in pixels. Defaults to the value of the `font_size`
            property.
        color (None | str | Unset):
        background_color (None | str | Unset):
        font_family (None | str | Unset): (**default=`"Verdana"`**) Font family. Provide [family-
            name](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#family-name-value)
            for a specific font. "generic-family" values like e.g. "sans-serif" will not work.
        style (None | TextStyle | Unset):
        align (HorizontalAlign | None | Unset):
        wrap (None | TextWrapMode | Unset):
        weight (None | TextWeight | Unset):
    """

    text: str
    font_size: float
    type_: TextType
    id: None | str | Unset = UNSET
    width: float | None | Unset = UNSET
    height: float | None | Unset = UNSET
    max_width: float | None | Unset = UNSET
    max_height: float | None | Unset = UNSET
    line_height: float | None | Unset = UNSET
    color: None | str | Unset = UNSET
    background_color: None | str | Unset = UNSET
    font_family: None | str | Unset = UNSET
    style: None | TextStyle | Unset = UNSET
    align: HorizontalAlign | None | Unset = UNSET
    wrap: None | TextWrapMode | Unset = UNSET
    weight: None | TextWeight | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        font_size = self.font_size

        type_ = self.type_.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        width: float | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: float | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        max_width: float | None | Unset
        if isinstance(self.max_width, Unset):
            max_width = UNSET
        else:
            max_width = self.max_width

        max_height: float | None | Unset
        if isinstance(self.max_height, Unset):
            max_height = UNSET
        else:
            max_height = self.max_height

        line_height: float | None | Unset
        if isinstance(self.line_height, Unset):
            line_height = UNSET
        else:
            line_height = self.line_height

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        background_color: None | str | Unset
        if isinstance(self.background_color, Unset):
            background_color = UNSET
        else:
            background_color = self.background_color

        font_family: None | str | Unset
        if isinstance(self.font_family, Unset):
            font_family = UNSET
        else:
            font_family = self.font_family

        style: None | str | Unset
        if isinstance(self.style, Unset):
            style = UNSET
        elif isinstance(self.style, TextStyle):
            style = self.style.value
        else:
            style = self.style

        align: None | str | Unset
        if isinstance(self.align, Unset):
            align = UNSET
        elif isinstance(self.align, HorizontalAlign):
            align = self.align.value
        else:
            align = self.align

        wrap: None | str | Unset
        if isinstance(self.wrap, Unset):
            wrap = UNSET
        elif isinstance(self.wrap, TextWrapMode):
            wrap = self.wrap.value
        else:
            wrap = self.wrap

        weight: None | str | Unset
        if isinstance(self.weight, Unset):
            weight = UNSET
        elif isinstance(self.weight, TextWeight):
            weight = self.weight.value
        else:
            weight = self.weight

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "text": text,
            "font_size": font_size,
            "type": type_,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if max_width is not UNSET:
            field_dict["max_width"] = max_width
        if max_height is not UNSET:
            field_dict["max_height"] = max_height
        if line_height is not UNSET:
            field_dict["line_height"] = line_height
        if color is not UNSET:
            field_dict["color"] = color
        if background_color is not UNSET:
            field_dict["background_color"] = background_color
        if font_family is not UNSET:
            field_dict["font_family"] = font_family
        if style is not UNSET:
            field_dict["style"] = style
        if align is not UNSET:
            field_dict["align"] = align
        if wrap is not UNSET:
            field_dict["wrap"] = wrap
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        font_size = d.pop("font_size")

        type_ = TextType(d.pop("type"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_width(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))

        def _parse_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_max_width(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_width = _parse_max_width(d.pop("max_width", UNSET))

        def _parse_max_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_height = _parse_max_height(d.pop("max_height", UNSET))

        def _parse_line_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        line_height = _parse_line_height(d.pop("line_height", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_background_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        background_color = _parse_background_color(d.pop("background_color", UNSET))

        def _parse_font_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        font_family = _parse_font_family(d.pop("font_family", UNSET))

        def _parse_style(data: object) -> None | TextStyle | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                style_type_1 = TextStyle(data)

                return style_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextStyle | Unset, data)

        style = _parse_style(d.pop("style", UNSET))

        def _parse_align(data: object) -> HorizontalAlign | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                align_type_1 = HorizontalAlign(data)

                return align_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HorizontalAlign | None | Unset, data)

        align = _parse_align(d.pop("align", UNSET))

        def _parse_wrap(data: object) -> None | TextWrapMode | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wrap_type_1 = TextWrapMode(data)

                return wrap_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextWrapMode | Unset, data)

        wrap = _parse_wrap(d.pop("wrap", UNSET))

        def _parse_weight(data: object) -> None | TextWeight | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_type_1 = TextWeight(data)

                return weight_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextWeight | Unset, data)

        weight = _parse_weight(d.pop("weight", UNSET))

        text = cls(
            text=text,
            font_size=font_size,
            type_=type_,
            id=id,
            width=width,
            height=height,
            max_width=max_width,
            max_height=max_height,
            line_height=line_height,
            color=color,
            background_color=background_color,
            font_family=font_family,
            style=style,
            align=align,
            wrap=wrap,
            weight=weight,
        )

        return text
