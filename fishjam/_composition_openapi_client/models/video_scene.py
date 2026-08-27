from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.image import Image
    from ..models.input_stream import InputStream
    from ..models.rescaler import Rescaler
    from ..models.text import Text
    from ..models.tiles import Tiles
    from ..models.view import View


T = TypeVar("T", bound="VideoScene")


@_attrs_define
class VideoScene:
    """
    Attributes:
        root (Image | InputStream | Rescaler | Text | Tiles | View):
    """

    root: Image | InputStream | Rescaler | Text | Tiles | View

    def to_dict(self) -> dict[str, Any]:
        from ..models.input_stream import InputStream
        from ..models.rescaler import Rescaler
        from ..models.text import Text
        from ..models.tiles import Tiles
        from ..models.view import View

        root: dict[str, Any]
        if isinstance(self.root, InputStream):
            root = self.root.to_dict()
        elif isinstance(self.root, View):
            root = self.root.to_dict()
        elif isinstance(self.root, Text):
            root = self.root.to_dict()
        elif isinstance(self.root, Tiles):
            root = self.root.to_dict()
        elif isinstance(self.root, Rescaler):
            root = self.root.to_dict()
        else:
            root = self.root.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({
            "root": root,
        })

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image import Image
        from ..models.input_stream import InputStream
        from ..models.rescaler import Rescaler
        from ..models.text import Text
        from ..models.tiles import Tiles
        from ..models.view import View

        d = dict(src_dict)

        def _parse_root(
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

        root = _parse_root(d.pop("root"))

        video_scene = cls(
            root=root,
        )

        return video_scene
