from fishjam import FishjamClient, RoomOptions


class FishjamService:
    def __init__(self, fishjam_id: str, management_token: str):
        self.fishjam = FishjamClient(fishjam_id, management_token)
        self.livestream_id = self.fishjam.create_room(
            RoomOptions(room_type="livestream")
        ).id

    def livestream_whip_url(self) -> str:
        return self.fishjam.livestream_whip_url()

    def livestream_whep_url(self) -> str:
        return self.fishjam.livestream_whep_url()

    def create_streamer_token(self) -> str:
        return self.fishjam.create_livestream_streamer_token(self.livestream_id)

    def create_viewer_token(self) -> str:
        return self.fishjam.create_livestream_viewer_token(self.livestream_id)

    def cleanup(self) -> None:
        self.fishjam.delete_room(self.livestream_id)
