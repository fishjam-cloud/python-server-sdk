from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.overflow import Overflow
from ..models.view_direction import ViewDirection
from ..models.view_type import ViewType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.box_shadow import BoxShadow
    from ..models.image import Image
    from ..models.input_stream import InputStream
    from ..models.rescaler import Rescaler
    from ..models.text import Text
    from ..models.tiles import Tiles
    from ..models.transition import Transition


T = TypeVar("T", bound="View")


@_attrs_define
class View:
    """
    Attributes:
        type_ (ViewType):
        id (None | str | Unset):
        children (list[Image | InputStream | Rescaler | Text | Tiles | View] | None | Unset): List of component's
            children.
        width (float | None | Unset): Width of a component in pixels (without a border). Exact behavior might be
            different
            based on the parent component:
            - If the parent component is a layout, check sections "Absolute positioning" and "Static
              positioning" of that component.
            - If the parent component is not a layout, then this field is required.
        height (float | None | Unset): Height of a component in pixels (without a border). Exact behavior might be
            different
            based on the parent component:
            - If the parent component is a layout, check sections "Absolute positioning" and "Static
              positioning" of that component.
            - If the parent component is not a layout, then this field is required.
        direction (None | Unset | ViewDirection):
        top (float | None | Unset): Distance in pixels between this component's top edge and its parent's top edge
            (including a border).
            If this field is defined, then the component will ignore a layout defined by its parent.
        left (float | None | Unset): Distance in pixels between this component's left edge and its parent's left edge
            (including a border).
            If this field is defined, this element will be absolutely positioned, instead of being
            laid out by its parent.
        bottom (float | None | Unset): Distance in pixels between the bottom edge of this component and the bottom edge
            of its
            parent (including a border). If this field is defined, this element will be absolutely
            positioned, instead of being laid out by its parent.
        right (float | None | Unset): Distance in pixels between this component's right edge and its parent's right
            edge.
            If this field is defined, this element will be absolutely positioned, instead of being
            laid out by its parent.
        rotation (float | None | Unset): Rotation of a component in degrees. If this field is defined, this element will
            be
            absolutely positioned, instead of being laid out by its parent.
        transition (None | Transition | Unset):
        overflow (None | Overflow | Unset):
        background_color (None | str | Unset):
        border_radius (float | None | Unset): (**default=`0.0`**) Radius of a rounded corner.
        border_width (float | None | Unset): (**default=`0.0`**) Border width.
        border_color (None | str | Unset):
        box_shadow (list[BoxShadow] | None | Unset): List of box shadows.
        padding (float | None | Unset): (**default=`0.0`**) Padding for all sides of the component.
        padding_vertical (float | None | Unset): (**default=`0.0`**) Padding for the top and bottom of the component.
        padding_horizontal (float | None | Unset): (**default=`0.0`**) Padding for the left and right of the component.
        padding_top (float | None | Unset): (**default=`0.0`**) Padding on top side in pixels.
        padding_right (float | None | Unset): (**default=`0.0`**) Padding on right side in pixels.
        padding_bottom (float | None | Unset): (**default=`0.0`**) Padding on bottom side in pixels.
        padding_left (float | None | Unset): (**default=`0.0`**) Padding on left side in pixels.
    """

    type_: ViewType
    id: None | str | Unset = UNSET
    children: (
        list[Image | InputStream | Rescaler | Text | Tiles | View] | None | Unset
    ) = UNSET
    width: float | None | Unset = UNSET
    height: float | None | Unset = UNSET
    direction: None | Unset | ViewDirection = UNSET
    top: float | None | Unset = UNSET
    left: float | None | Unset = UNSET
    bottom: float | None | Unset = UNSET
    right: float | None | Unset = UNSET
    rotation: float | None | Unset = UNSET
    transition: None | Transition | Unset = UNSET
    overflow: None | Overflow | Unset = UNSET
    background_color: None | str | Unset = UNSET
    border_radius: float | None | Unset = UNSET
    border_width: float | None | Unset = UNSET
    border_color: None | str | Unset = UNSET
    box_shadow: list[BoxShadow] | None | Unset = UNSET
    padding: float | None | Unset = UNSET
    padding_vertical: float | None | Unset = UNSET
    padding_horizontal: float | None | Unset = UNSET
    padding_top: float | None | Unset = UNSET
    padding_right: float | None | Unset = UNSET
    padding_bottom: float | None | Unset = UNSET
    padding_left: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.input_stream import InputStream
        from ..models.rescaler import Rescaler
        from ..models.text import Text
        from ..models.tiles import Tiles
        from ..models.transition import Transition

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

        direction: None | str | Unset
        if isinstance(self.direction, Unset):
            direction = UNSET
        elif isinstance(self.direction, ViewDirection):
            direction = self.direction.value
        else:
            direction = self.direction

        top: float | None | Unset
        if isinstance(self.top, Unset):
            top = UNSET
        else:
            top = self.top

        left: float | None | Unset
        if isinstance(self.left, Unset):
            left = UNSET
        else:
            left = self.left

        bottom: float | None | Unset
        if isinstance(self.bottom, Unset):
            bottom = UNSET
        else:
            bottom = self.bottom

        right: float | None | Unset
        if isinstance(self.right, Unset):
            right = UNSET
        else:
            right = self.right

        rotation: float | None | Unset
        if isinstance(self.rotation, Unset):
            rotation = UNSET
        else:
            rotation = self.rotation

        transition: dict[str, Any] | None | Unset
        if isinstance(self.transition, Unset):
            transition = UNSET
        elif isinstance(self.transition, Transition):
            transition = self.transition.to_dict()
        else:
            transition = self.transition

        overflow: None | str | Unset
        if isinstance(self.overflow, Unset):
            overflow = UNSET
        elif isinstance(self.overflow, Overflow):
            overflow = self.overflow.value
        else:
            overflow = self.overflow

        background_color: None | str | Unset
        if isinstance(self.background_color, Unset):
            background_color = UNSET
        else:
            background_color = self.background_color

        border_radius: float | None | Unset
        if isinstance(self.border_radius, Unset):
            border_radius = UNSET
        else:
            border_radius = self.border_radius

        border_width: float | None | Unset
        if isinstance(self.border_width, Unset):
            border_width = UNSET
        else:
            border_width = self.border_width

        border_color: None | str | Unset
        if isinstance(self.border_color, Unset):
            border_color = UNSET
        else:
            border_color = self.border_color

        box_shadow: list[dict[str, Any]] | None | Unset
        if isinstance(self.box_shadow, Unset):
            box_shadow = UNSET
        elif isinstance(self.box_shadow, list):
            box_shadow = []
            for box_shadow_type_0_item_data in self.box_shadow:
                box_shadow_type_0_item = box_shadow_type_0_item_data.to_dict()
                box_shadow.append(box_shadow_type_0_item)

        else:
            box_shadow = self.box_shadow

        padding: float | None | Unset
        if isinstance(self.padding, Unset):
            padding = UNSET
        else:
            padding = self.padding

        padding_vertical: float | None | Unset
        if isinstance(self.padding_vertical, Unset):
            padding_vertical = UNSET
        else:
            padding_vertical = self.padding_vertical

        padding_horizontal: float | None | Unset
        if isinstance(self.padding_horizontal, Unset):
            padding_horizontal = UNSET
        else:
            padding_horizontal = self.padding_horizontal

        padding_top: float | None | Unset
        if isinstance(self.padding_top, Unset):
            padding_top = UNSET
        else:
            padding_top = self.padding_top

        padding_right: float | None | Unset
        if isinstance(self.padding_right, Unset):
            padding_right = UNSET
        else:
            padding_right = self.padding_right

        padding_bottom: float | None | Unset
        if isinstance(self.padding_bottom, Unset):
            padding_bottom = UNSET
        else:
            padding_bottom = self.padding_bottom

        padding_left: float | None | Unset
        if isinstance(self.padding_left, Unset):
            padding_left = UNSET
        else:
            padding_left = self.padding_left

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
        if direction is not UNSET:
            field_dict["direction"] = direction
        if top is not UNSET:
            field_dict["top"] = top
        if left is not UNSET:
            field_dict["left"] = left
        if bottom is not UNSET:
            field_dict["bottom"] = bottom
        if right is not UNSET:
            field_dict["right"] = right
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
        if transition is not UNSET:
            field_dict["transition"] = transition
        if overflow is not UNSET:
            field_dict["overflow"] = overflow
        if background_color is not UNSET:
            field_dict["background_color"] = background_color
        if border_radius is not UNSET:
            field_dict["border_radius"] = border_radius
        if border_width is not UNSET:
            field_dict["border_width"] = border_width
        if border_color is not UNSET:
            field_dict["border_color"] = border_color
        if box_shadow is not UNSET:
            field_dict["box_shadow"] = box_shadow
        if padding is not UNSET:
            field_dict["padding"] = padding
        if padding_vertical is not UNSET:
            field_dict["padding_vertical"] = padding_vertical
        if padding_horizontal is not UNSET:
            field_dict["padding_horizontal"] = padding_horizontal
        if padding_top is not UNSET:
            field_dict["padding_top"] = padding_top
        if padding_right is not UNSET:
            field_dict["padding_right"] = padding_right
        if padding_bottom is not UNSET:
            field_dict["padding_bottom"] = padding_bottom
        if padding_left is not UNSET:
            field_dict["padding_left"] = padding_left

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.box_shadow import BoxShadow
        from ..models.image import Image
        from ..models.input_stream import InputStream
        from ..models.rescaler import Rescaler
        from ..models.text import Text
        from ..models.tiles import Tiles
        from ..models.transition import Transition

        d = dict(src_dict)
        type_ = ViewType(d.pop("type"))

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

        def _parse_direction(data: object) -> None | Unset | ViewDirection:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                direction_type_1 = ViewDirection(data)

                return direction_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViewDirection, data)

        direction = _parse_direction(d.pop("direction", UNSET))

        def _parse_top(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        top = _parse_top(d.pop("top", UNSET))

        def _parse_left(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        left = _parse_left(d.pop("left", UNSET))

        def _parse_bottom(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bottom = _parse_bottom(d.pop("bottom", UNSET))

        def _parse_right(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        right = _parse_right(d.pop("right", UNSET))

        def _parse_rotation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rotation = _parse_rotation(d.pop("rotation", UNSET))

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

        def _parse_overflow(data: object) -> None | Overflow | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                overflow_type_1 = Overflow(data)

                return overflow_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Overflow | Unset, data)

        overflow = _parse_overflow(d.pop("overflow", UNSET))

        def _parse_background_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        background_color = _parse_background_color(d.pop("background_color", UNSET))

        def _parse_border_radius(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        border_radius = _parse_border_radius(d.pop("border_radius", UNSET))

        def _parse_border_width(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        border_width = _parse_border_width(d.pop("border_width", UNSET))

        def _parse_border_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        border_color = _parse_border_color(d.pop("border_color", UNSET))

        def _parse_box_shadow(data: object) -> list[BoxShadow] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                box_shadow_type_0 = []
                _box_shadow_type_0 = data
                for box_shadow_type_0_item_data in _box_shadow_type_0:
                    box_shadow_type_0_item = BoxShadow.from_dict(
                        box_shadow_type_0_item_data
                    )

                    box_shadow_type_0.append(box_shadow_type_0_item)

                return box_shadow_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BoxShadow] | None | Unset, data)

        box_shadow = _parse_box_shadow(d.pop("box_shadow", UNSET))

        def _parse_padding(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        padding = _parse_padding(d.pop("padding", UNSET))

        def _parse_padding_vertical(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        padding_vertical = _parse_padding_vertical(d.pop("padding_vertical", UNSET))

        def _parse_padding_horizontal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        padding_horizontal = _parse_padding_horizontal(
            d.pop("padding_horizontal", UNSET)
        )

        def _parse_padding_top(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        padding_top = _parse_padding_top(d.pop("padding_top", UNSET))

        def _parse_padding_right(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        padding_right = _parse_padding_right(d.pop("padding_right", UNSET))

        def _parse_padding_bottom(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        padding_bottom = _parse_padding_bottom(d.pop("padding_bottom", UNSET))

        def _parse_padding_left(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        padding_left = _parse_padding_left(d.pop("padding_left", UNSET))

        view = cls(
            type_=type_,
            id=id,
            children=children,
            width=width,
            height=height,
            direction=direction,
            top=top,
            left=left,
            bottom=bottom,
            right=right,
            rotation=rotation,
            transition=transition,
            overflow=overflow,
            background_color=background_color,
            border_radius=border_radius,
            border_width=border_width,
            border_color=border_color,
            box_shadow=box_shadow,
            padding=padding,
            padding_vertical=padding_vertical,
            padding_horizontal=padding_horizontal,
            padding_top=padding_top,
            padding_right=padding_right,
            padding_bottom=padding_bottom,
            padding_left=padding_left,
        )

        return view
