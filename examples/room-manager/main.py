import logging
from flask import Flask

from routes import setup_routes
from arguments import parse_arguments
from room_service import RoomService


app = Flask(__name__)
app.logger.setLevel(logging.INFO)


if __name__ == "__main__":
    args = parse_arguments()

    room_service = RoomService(args, app.logger)

    setup_routes(app, room_service)

    app.run()
