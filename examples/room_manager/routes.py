from dataclasses import asdict

from flask import Flask, abort, jsonify, request

from fishjam import receive_binary

from .room_service import RoomService


def setup_routes(app: Flask, room_service: RoomService):
    @app.route("/health", methods=["GET"])
    def health_check():
        status = "OK"
        return jsonify({"status": status})

    @app.get("/api/rooms/<room_name>/users/<peer_name>")
    def get_room_params(room_name, peer_name):
        access_data = room_service.get_peer_access(room_name, peer_name)
        response = asdict(access_data)
        response["peerToken"] = response.pop("peer_token")

        return jsonify(response)

    @app.get("/api/rooms")
    def get_room_query():
        room_name = request.args.get("roomName")
        peer_name = request.args.get("peerName")

        if not room_name or not peer_name:
            return abort(400)

        access_data = room_service.get_peer_access(room_name, peer_name)
        response = asdict(access_data)

        return jsonify(response)

    @app.get("/api/rooms/<room_name>/start-recording")
    def startRecording():
        response = jsonify({"error": "Not yet implemented"})
        response.status_code = 501

        return response

    @app.post("/api/rooms/webhook")
    def webhook():
        notification = receive_binary(request.data)

        if notification:
            room_service.handle_notification(notification)

        return "Webhook Notification Received", 200
