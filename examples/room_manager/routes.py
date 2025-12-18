from dataclasses import asdict

from flask import Flask, abort, jsonify, request
from room_service import RoomService

from fishjam import receive_binary
from fishjam.room import RoomType


def setup_routes(app: Flask, room_service: RoomService):
    @app.route("/health", methods=["GET"])
    def health_check():
        status = "OK"
        return jsonify({"status": status})

    @app.get("/api/rooms")
    def get_room_query():
        room_name = request.args.get("roomName")
        raw_room_type = request.args.get("roomType")
        peer_name = request.args.get("peerName")

        if not room_name or not peer_name:
            return abort(400)

        try:
            room_type = RoomType(raw_room_type) if raw_room_type else None
        except ValueError:
            return abort(400)

        access_data = room_service.get_peer_access(room_name, peer_name, room_type)
        response = asdict(access_data)

        response["peerToken"] = response.pop("peer_token")

        return jsonify(response)

    @app.post("/api/rooms/webhook")
    def webhook():
        notification = receive_binary(request.data)

        if notification:
            room_service.handle_notification(notification)

        return "Webhook Notification Received", 200
