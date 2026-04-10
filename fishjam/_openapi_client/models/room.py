from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.composition_info import CompositionInfo
    from ..models.peer import Peer
    from ..models.room_config import RoomConfig


T = TypeVar("T", bound="Room")


@_attrs_define
class Room:
    """Description of the room state

    Attributes:
        config (RoomConfig): Room configuration
        id (str): Room ID Example: room-1.
        peers (list[Peer]): List of all peers
        composition_info (CompositionInfo | None | Unset): Composition and track forwarding state for the room
    """

    config: RoomConfig
    id: str
    peers: list[Peer]
    composition_info: CompositionInfo | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.composition_info import CompositionInfo

        config = self.config.to_dict()

        id = self.id

        peers = []
        for peers_item_data in self.peers:
            peers_item = peers_item_data.to_dict()
            peers.append(peers_item)

        composition_info: dict[str, Any] | None | Unset
        if isinstance(self.composition_info, Unset):
            composition_info = UNSET
        elif isinstance(self.composition_info, CompositionInfo):
            composition_info = self.composition_info.to_dict()
        else:
            composition_info = self.composition_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "config": config,
            "id": id,
            "peers": peers,
        })
        if composition_info is not UNSET:
            field_dict["compositionInfo"] = composition_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.composition_info import CompositionInfo
        from ..models.peer import Peer
        from ..models.room_config import RoomConfig

        d = dict(src_dict)
        config = RoomConfig.from_dict(d.pop("config"))

        id = d.pop("id")

        peers = []
        _peers = d.pop("peers")
        for peers_item_data in _peers:
            peers_item = Peer.from_dict(peers_item_data)

            peers.append(peers_item)

        def _parse_composition_info(data: object) -> CompositionInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_composition_info_type_0 = CompositionInfo.from_dict(
                    data
                )

                return componentsschemas_composition_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompositionInfo | None | Unset, data)

        composition_info = _parse_composition_info(d.pop("compositionInfo", UNSET))

        room = cls(
            config=config,
            id=id,
            peers=peers,
            composition_info=composition_info,
        )

        room.additional_properties = d
        return room

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
