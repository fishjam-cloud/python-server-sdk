from pathlib import Path

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route
from starlette.templating import Jinja2Templates

from .room_service import RoomService

room_service = RoomService()
templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent.parent / "templates"))


async def create_peer(request: Request) -> Response:
    try:
        body = await request.json()
        room_name = body.get("room_name")
        peer_name = body.get("peer_name")

        if not room_name or not peer_name:
            return JSONResponse(
                {"error": "room_name and peer_name are required"},
                status_code=400
            )

        peer, token = room_service.create_peer()

        return JSONResponse({
            "peer_id": peer.id,
            "token": token,
            "room_name": room_name,
            "peer_name": peer_name
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

async def subscribe_peer(request: Request) -> Response:
    try:
        body = await request.json()
        peer_id = body.get("peer_id")
        target_peer_id = body.get("target_peer_id")

        if not peer_id or not target_peer_id:
            return JSONResponse(
                {"error": "peer_id and target_peer_id are required"},
                status_code=400
            )

        room_service.subscibe_peer(peer_id, target_peer_id)
        return JSONResponse({"status": "subscribed"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def subscribe_tracks(request: Request) -> Response:
    try:
        body = await request.json()
        peer_id = body.get("peer_id")
        track_ids = body.get("track_ids")

        if not peer_id or not track_ids:
            return JSONResponse(
                {"error": "peer_id and track_ids are required"},
                status_code=400
            )

        room_service.subscribe_tracks(peer_id, track_ids)
        return JSONResponse({"status": "subscribed"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

async def serve_index(request: Request) -> Response:
    return templates.TemplateResponse("index.html", {"request": request})


routes = [
    Route("/", serve_index, methods=["GET"]),
    Route("/api/peers", create_peer, methods=["POST"]),
    Route("/api/subscribe_peer", subscribe_peer, methods=["POST"]),
    Route("/api/subscribe_tracks", subscribe_tracks, methods=["POST"]),
]

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = Starlette(
    routes=routes,
    middleware=middleware,
)