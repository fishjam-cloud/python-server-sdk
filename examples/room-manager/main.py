import logging

from arguments import parse_arguments
from flask import Flask
from room_service import RoomService
from routes import setup_routes

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


if __name__ == "__main__":
    args = parse_arguments()

    room_service = RoomService(args, app.logger)

    setup_routes(app, room_service)

    app.run()
