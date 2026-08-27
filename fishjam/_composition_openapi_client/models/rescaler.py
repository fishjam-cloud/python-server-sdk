from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.horizontal_align import HorizontalAlign
from ..models.rescale_mode import RescaleMode
from ..models.rescaler_type import RescalerType
from ..models.vertical_align import VerticalAlign
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.box_shadow import BoxShadow
    from ..models.image import Image
    from ..models.input_stream import InputStream
    from ..models.text import Text
    from ..models.tiles import Tiles
    from ..models.transition import Transition
    from ..models.view import View


T = TypeVar("T", bound="Rescaler")


@_attrs_define
class Rescaler:
    """
    Attributes:
        child (Image | InputStream | Rescaler | Text | Tiles | View):
        type_ (RescalerType):
        id (None | str | Unset):
        mode (None | RescaleMode | Unset):
        horizontal_align (HorizontalAlign | None | Unset):
        vertical_align (None | Unset | VerticalAlign):
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
        border_radius (float | None | Unset): (**default=`0.0`**) Radius of a rounded corner.
        border_width (float | None | Unset): (**default=`0.0`**) Border width.
        border_color (None | str | Unset):
        box_shadow (list[BoxShadow] | None | Unset): List of box shadows.
    """

    child: Image | InputStream | Rescaler | Text | Tiles | View
    type_: RescalerType
    id: None | str | Unset = UNSET
    mode: None | RescaleMode | Unset = UNSET
    horizontal_align: HorizontalAlign | None | Unset = UNSET
    vertical_align: None | Unset | VerticalAlign = UNSET
    width: float | None | Unset = UNSET
    height: float | None | Unset = UNSET
    top: float | None | Unset = UNSET
    left: float | None | Unset = UNSET
    bottom: float | None | Unset = UNSET
    right: float | None | Unset = UNSET
    rotation: float | None | Unset = UNSET
    transition: None | Transition | Unset = UNSET
    border_radius: float | None | Unset = UNSET
    border_width: float | None | Unset = UNSET
    border_color: None | str | Unset = UNSET
    box_shadow: list[BoxShadow] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.input_stream import InputStream
        from ..models.text import Text
        from ..models.tiles import Tiles
        from ..models.transition import Transition
        from ..models.view import View

        child: dict[str, Any]
        if isinstance(self.child, InputStream):
            child = self.child.to_dict()
        elif isinstance(self.child, View):
            child = self.child.to_dict()
        elif isinstance(self.child, Text):
            child = self.child.to_dict()
        elif isinstance(self.child, Tiles):
            child = self.child.to_dict()
        elif isinstance(self.child, Rescaler):
            child = self.child.to_dict()
        else:
            child = self.child.to_dict()

        type_ = self.type_.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, RescaleMode):
            mode = self.mode.value
        else:
            mode = self.mode

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

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "child": child,
            "type": type_,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if horizontal_align is not UNSET:
            field_dict["horizontal_align"] = horizontal_align
        if vertical_align is not UNSET:
            field_dict["vertical_align"] = vertical_align
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
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
        if border_radius is not UNSET:
            field_dict["border_radius"] = border_radius
        if border_width is not UNSET:
            field_dict["border_width"] = border_width
        if border_color is not UNSET:
            field_dict["border_color"] = border_color
        if box_shadow is not UNSET:
            field_dict["box_shadow"] = box_shadow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.box_shadow import BoxShadow
        from ..models.image import Image
        from ..models.input_stream import InputStream
        from ..models.text import Text
        from ..models.tiles import Tiles
        from ..models.transition import Transition
        from ..models.view import View

        d = dict(src_dict)

        def _parse_child(
            data: object,
        ) -> Image | InputStream | Rescaler | Text | Tiles | View:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_type_0 = InputStream.from_dict(data)

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
                componentsschemas_component_type_4 = Rescaler.from_dict(data)

                return componentsschemas_component_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_component_type_5 = Image.from_dict(data)

            return componentsschemas_component_type_5

        child = _parse_child(d.pop("child"))

        type_ = RescalerType(d.pop("type"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_mode(data: object) -> None | RescaleMode | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = RescaleMode(data)

                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RescaleMode | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))

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

        rescaler = cls(
            child=child,
            type_=type_,
            id=id,
            mode=mode,
            horizontal_align=horizontal_align,
            vertical_align=vertical_align,
            width=width,
            height=height,
            top=top,
            left=left,
            bottom=bottom,
            right=right,
            rotation=rotation,
            transition=transition,
            border_radius=border_radius,
            border_width=border_width,
            border_color=border_color,
            box_shadow=box_shadow,
        )

        return rescaler
