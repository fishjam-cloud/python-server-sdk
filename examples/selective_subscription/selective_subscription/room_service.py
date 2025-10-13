from typing import List

from fishjam import FishjamClient, Peer, PeerOptions, Room, RoomOptions
from fishjam.errors import NotFoundError

from .config import FISHJAM_ID, FISHJAM_TOKEN


class RoomService:
    def __init__(self):
        self.fishjam = FishjamClient(FISHJAM_ID, FISHJAM_TOKEN)
        self.room = self.fishjam.create_room(RoomOptions(
            max_peers=10,
            room_type="conference"
        ))

    def get_or_create_room(self) -> Room:
        if self.room:
            try:
                room = self.fishjam.get_room(self.room.id)
                return room
            except NotFoundError:
                pass

        return self.fishjam.create_room()

    def create_peer(self) -> tuple[Peer, str]:
        room = self.get_or_create_room()
        options = PeerOptions(subscribe_mode="manual")
        peer, token = self.fishjam.create_peer(room.id, options)
        return peer, token

    def subscibe_peer(self, peer_id: str, target_peer_id: str):
        room = self.get_or_create_room()
        self.fishjam.subscribe_peer(room.id, peer_id, target_peer_id)

    def subscribe_tracks(self, peer_id: str, track_ids: List[str]):
        room = self.get_or_create_room()
        self.fishjam.subscribe_tracks(room.id, peer_id, track_ids)

    def get_peer_session(self, peer_id: str):
        room = self.get_or_create_room()
        for p in room.peers:
            if p.id == peer_id:
                class _Session:
                    def __init__(self):
                        self.subscribed_peers: set[str] = set()

                return _Session()

        return None
