from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.horizontal_align import HorizontalAlign
from ..models.tiles_type import TilesType
from ..models.vertical_align import VerticalAlign
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image import Image
    from ..models.input_stream import InputStream
    from ..models.rescaler import Rescaler
    from ..models.text import Text
    from ..models.transition import Transition
    from ..models.view import View


T = TypeVar("T", bound="Tiles")


@_attrs_define
class Tiles:
    """
    Attributes:
        type_ (TilesType):
        id (None | str | Unset):
        children (list[Image | InputStream | Rescaler | Text | Tiles | View] | None | Unset): List of component's
            children.
        width (float | None | Unset): Width of a component in pixels. Exact behavior might be different based on the
            parent
            component:
            - If the parent component is a layout, check sections "Absolute positioning" and "Static
              positioning" of that component.
            - If the parent component is not a layout, then this field is required.
        height (float | None | Unset): Height of a component in pixels. Exact behavior might be different based on the
            parent
            component:
            - If the parent component is a layout, check sections "Absolute positioning" and "Static
              positioning" of that component.
            - If the parent component is not a layout, then this field is required.
        background_color (None | str | Unset):
        tile_aspect_ratio (None | str | Unset):
        margin (float | None | Unset): (**default=`0`**) Margin of each tile in pixels.
        padding (float | None | Unset): (**default=`0`**) Padding on each tile in pixels.
        horizontal_align (HorizontalAlign | None | Unset):
        vertical_align (None | Unset | VerticalAlign):
        transition (None | Transition | Unset):
    """

    type_: TilesType
    id: None | str | Unset = UNSET
    children: (
        list[Image | InputStream | Rescaler | Text | Tiles | View] | None | Unset
    ) = UNSET
    width: float | None | Unset = UNSET
    height: float | None | Unset = UNSET
    background_color: None | str | Unset = UNSET
    tile_aspect_ratio: None | str | Unset = UNSET
    margin: float | None | Unset = UNSET
    padding: float | None | Unset = UNSET
    horizontal_align: HorizontalAlign | None | Unset = UNSET
    vertical_align: None | Unset | VerticalAlign = UNSET
    transition: None | Transition | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.input_stream import InputStream
        from ..models.rescaler import Rescaler
        from ..models.text import Text
        from ..models.transition import Transition
        from ..models.view import View

        type_ = self.type_.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        children: list[dict[str, Any]] | None | Unset
        if isinstance(self.children, Unset):
            children = UNSET
        elif isinstance(self.children, list):
            children = []
            for children_type_0_item_data in self.children:
                children_type_0_item: dict[str, Any]
                if isinstance(children_type_0_item_data, InputStream):
                    children_type_0_item = children_type_0_item_data.to_dict()
                elif isinstance(children_type_0_item_data, View):
                    children_type_0_item = children_type_0_item_data.to_dict()
                elif isinstance(children_type_0_item_data, Text):
                    children_type_0_item = children_type_0_item_data.to_dict()
                elif isinstance(children_type_0_item_data, Tiles):
                    children_type_0_item = children_type_0_item_data.to_dict()
                elif isinstance(children_type_0_item_data, Rescaler):
                    children_type_0_item = children_type_0_item_data.to_dict()
                else:
                    children_type_0_item = children_type_0_item_data.to_dict()

                children.append(children_type_0_item)

        else:
            children = self.children

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

        background_color: None | str | Unset
        if isinstance(self.background_color, Unset):
            background_color = UNSET
        else:
            background_color = self.background_color

        tile_aspect_ratio: None | str | Unset
        if isinstance(self.tile_aspect_ratio, Unset):
            tile_aspect_ratio = UNSET
        else:
            tile_aspect_ratio = self.tile_aspect_ratio

        margin: float | None | Unset
        if isinstance(self.margin, Unset):
            margin = UNSET
        else:
            margin = self.margin

        padding: float | None | Unset
        if isinstance(self.padding, Unset):
            padding = UNSET
        else:
            padding = self.padding

        horizontal_align: None | str | Unset
        if isinstance(self.horizontal_align, Unset):
            horizontal_align = UNSET
        elif isinstance(self.horizontal_align, HorizontalAlign):
            horizontal_align = self.horizontal_align.value
        else:
            horizontal_align = self.horizontal_align

        vertical_align: None | str | Unset
        if isinstance(self.vertical_align, Unset):
            vertical_align = UNSET
        elif isinstance(self.vertical_align, VerticalAlign):
            vertical_align = self.vertical_align.value
        else:
            vertical_align = self.vertical_align

        transition: dict[str, Any] | None | Unset
        if isinstance(self.transition, Unset):
            transition = UNSET
        elif isinstance(self.transition, Transition):
            transition = self.transition.to_dict()
        else:
            transition = self.transition

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if children is not UNSET:
            field_dict["children"] = children
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if background_color is not UNSET:
            field_dict["background_color"] = background_color
        if tile_aspect_ratio is not UNSET:
            field_dict["tile_aspect_ratio"] = tile_aspect_ratio
        if margin is not UNSET:
            field_dict["margin"] = margin
        if padding is not UNSET:
            field_dict["padding"] = padding
        if horizontal_align is not UNSET:
            field_dict["horizontal_align"] = horizontal_align
        if vertical_align is not UNSET:
            field_dict["vertical_align"] = vertical_align
        if transition is not UNSET:
            field_dict["transition"] = transition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image import Image
        from ..models.input_stream import InputStream
        from ..models.rescaler import Rescaler
        from ..models.text import Text
        from ..models.transition import Transition
        from ..models.view import View

        d = dict(src_dict)
        type_ = TilesType(d.pop("type"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_children(
            data: object,
        ) -> list[Image | InputStream | Rescaler | Text | Tiles | View] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = []
                _children_type_0 = data
                for children_type_0_item_data in _children_type_0:

                    def _parse_children_type_0_item(
                        data: object,
                    ) -> Image | InputStream | Rescaler | Text | Tiles | View:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_type_0 = InputStream.from_dict(
                                data
                            )

                            return componentsschemas_component_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_type_1 = View.from_dict(data)

                            return componentsschemas_component_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_type_2 = Text.from_dict(data)

                            return componentsschemas_component_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_type_3 = Tiles.from_dict(data)

                            return componentsschemas_component_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_type_4 = Rescaler.from_dict(
                                data
                            )

                            return componentsschemas_component_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_component_type_5 = Image.from_dict(data)

                        return componentsschemas_component_type_5

                    children_type_0_item = _parse_children_type_0_item(
                        children_type_0_item_data
                    )

                    children_type_0.append(children_type_0_item)

                return children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[Image | InputStream | Rescaler | Text | Tiles | View]
                | None
                | Unset,
                data,
            )

        children = _parse_children(d.pop("children", UNSET))

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

        def _parse_background_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        background_color = _parse_background_color(d.pop("background_color", UNSET))

        def _parse_tile_aspect_ratio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tile_aspect_ratio = _parse_tile_aspect_ratio(d.pop("tile_aspect_ratio", UNSET))

        def _parse_margin(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin = _parse_margin(d.pop("margin", UNSET))

        def _parse_padding(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        padding = _parse_padding(d.pop("padding", UNSET))

        def _parse_horizontal_align(data: object) -> HorizontalAlign | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                horizontal_align_type_1 = HorizontalAlign(data)

                return horizontal_align_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HorizontalAlign | None | Unset, data)

        horizontal_align = _parse_horizontal_align(d.pop("horizontal_align", UNSET))

        def _parse_vertical_align(data: object) -> None | Unset | VerticalAlign:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vertical_align_type_1 = VerticalAlign(data)

                return vertical_align_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VerticalAlign, data)

        vertical_align = _parse_vertical_align(d.pop("vertical_align", UNSET))

        def _parse_transition(data: object) -> None | Transition | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transition_type_1 = Transition.from_dict(data)

                return transition_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Transition | Unset, data)

        transition = _parse_transition(d.pop("transition", UNSET))

        tiles = cls(
            type_=type_,
            id=id,
            children=children,
            width=width,
            height=height,
            background_color=background_color,
            tile_aspect_ratio=tile_aspect_ratio,
            margin=margin,
            padding=padding,
            horizontal_align=horizontal_align,
            vertical_align=vertical_align,
            transition=transition,
        )

        return tiles
