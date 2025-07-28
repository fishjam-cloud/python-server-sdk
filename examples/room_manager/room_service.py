from argparse import Namespace
from dataclasses import dataclass
from logging import Logger
from typing import List

import betterproto

from fishjam import FishjamClient, PeerOptions, Room, RoomOptions
from fishjam._openapi_client.models import RoomConfigRoomType
from fishjam.events import ServerMessagePeerCrashed as PeerCrashed
from fishjam.events import ServerMessagePeerDeleted as PeerDeleted
from fishjam.events import ServerMessageRoomCrashed as RoomCrashed
from fishjam.events import ServerMessageRoomDeleted as RoomDeleted


@dataclass
class Resource:
    id: str
    name: str


@dataclass
class PeerAccess:
    room: Resource
    peer: Resource
    peer_token: str


class RoomService:
    def __init__(self, args: Namespace, logger: Logger):
        self.fishjam_client = FishjamClient(
            fishjam_id=args.fishjam_id,
            management_token=args.management_token,
            fishjam_url=args.fishjam_url,
        )
        self.room_name_to_room_id: dict[str, str] = {}
        self.peer_name_to_access: dict[str, PeerAccess] = {}
        self.logger = logger
        self.config = args

    def get_peer_access(
        self,
        room_name: str,
        username: str,
        room_type: RoomConfigRoomType | None,
    ) -> PeerAccess:
        room = self.__find_or_create_room(room_name, room_type)
        peer_access = self.peer_name_to_access.get(username)
        peer_in_room = self.__is_in_room(room, peer_access)

        self.logger.info(
            "Got room: %s", {"name": room_name, "id": room.id, "peers": room.peers}
        )

        if not peer_access or not peer_in_room:
            return self.__create_peer(room_name, username)

        self.logger.info("Peer exist: %s", username)

        return peer_access

    def handle_notification(self, notification: betterproto.Message):
        match notification:
            case PeerCrashed() | PeerDeleted():
                self.__remove_peer(notification.peer_id)
            case RoomCrashed() | RoomDeleted():
                self.__remove_room(notification.room_id)
            case _:
                pass

    def __find_or_create_room(
        self, room_name: str, room_type: RoomConfigRoomType | None
    ) -> Room:
        if room_name in self.room_name_to_room_id:
            self.logger.info("Room %s, already exists in the Fishjam", room_name)

            room_id = self.room_name_to_room_id[room_name]
            return self.fishjam_client.get_room(room_id=room_id)

        options = RoomOptions(
            max_peers=self.config.max_peers,
            webhook_url=self.config.webhook_url,
            room_type=room_type.value if room_type else "conference",
        )

        new_room = self.fishjam_client.create_room(options=options)

        self.room_name_to_room_id[room_name] = new_room.id

        self.logger.info("Room created: %s", new_room)

        return new_room

    def __create_peer(self, room_name: str, peer_name: str) -> PeerAccess:
        room_id = self.room_name_to_room_id[room_name]

        options = PeerOptions(
            enable_simulcast=self.config.enable_simulcast,
            metadata={"username": peer_name},
        )
        peer, token = self.fishjam_client.create_peer(room_id, options=options)

        peer_access = PeerAccess(
            room=Resource(id=room_id, name=room_name),
            peer=Resource(id=peer.id, name=peer_name),
            peer_token=token,
        )

        self.peer_name_to_access[peer_name] = peer_access

        self.logger.info("Peer created: %s", peer)

        return peer_access

    def __remove_room(self, room_id: str):
        room_name = self.__find_room_name(room_id)
        peer_accesses = self.__find_peer_access_by_room_id(room_id)

        if room_name:
            self.room_name_to_room_id.pop(room_name)
            self.logger.info(
                "Room deleted from cache. %s", {"name": room_name, "id": room_id}
            )
        else:
            self.logger.info("Room not found in cache, id: %s", room_id)

        for peer_access in peer_accesses:
            self.peer_name_to_access.pop(peer_access.peer.name)

    def __remove_peer(self, peer_id: str):
        peer_access = self.__find_peer_access(peer_id)

        if peer_access:
            self.peer_name_to_access.pop(peer_access.peer.name)
            self.logger.info(
                "Peer deleted from cache. %s",
                {"id": peer_id, "room_id": peer_access.room.id},
            )
        else:
            self.logger.info("Peer not found in cache, id: %s", peer_id)

    def __find_peer_access(self, peer_id) -> PeerAccess | None:
        peer_accesses = self.peer_name_to_access.values()
        peer_access = list(
            filter(lambda access: access.peer.id == peer_id, peer_accesses)
        )

        return peer_access[0] if peer_access else None

    def __find_peer_access_by_room_id(self, room_id: str) -> List[PeerAccess]:
        peer_accesses = self.peer_name_to_access.values()
        filtered_peer_accesses = list(
            filter(lambda access: access.room.id == room_id, peer_accesses)
        )

        return filtered_peer_accesses

    def __find_room_name(self, room_id: str) -> str | None:
        for name, r_id in self.room_name_to_room_id.items():
            if room_id == r_id:
                return name

        return None

    def __is_in_room(self, room: Room, peer_access: PeerAccess | None) -> bool:
        if not peer_access:
            return False

        return any(peer.id == peer_access.peer.id for peer in room.peers)
