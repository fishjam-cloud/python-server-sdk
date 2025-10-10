import json
from typing import Dict, Any

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route
from starlette.templating import Jinja2Templates

from .room_service import RoomService


# Initialize services
room_service = RoomService()
templates = Jinja2Templates(directory="templates")


async def create_peer(request: Request) -> Response:
    """Create a new peer in a room."""
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


async def get_available_peers(request: Request) -> Response:
    """Get peers available for subscription."""
    room_name = request.path_params.get("room_name")
    peer_id = request.query_params.get("peer_id")
    
    if not room_name:
        return JSONResponse({"error": "room_name is required"}, status_code=400)
    
    peers = room_service.get_available_peers(room_name, peer_id)
    
    return JSONResponse({
        "peers": [
            {
                "id": peer.id,
                "metadata": peer.metadata if peer.metadata else {},
                "tracks": [
                    {
                        "id": track["id"],
                        "type": track.get("type", "unknown")
                    }
                    for track in peer.tracks
                ]
            }
            for peer in peers
        ]
    })


async def toggle_subscription(request: Request) -> Response:
    """Toggle subscription to a peer's tracks."""
    try:
        body = await request.json()
        peer_id = body.get("peer_id")
        target_peer_id = body.get("target_peer_id")
        
        if not peer_id or not target_peer_id:
            return JSONResponse(
                {"error": "peer_id and target_peer_id are required"},
                status_code=400
            )
        
        subscribed = room_service.toggle_subscription(peer_id, target_peer_id)
        
        return JSONResponse({
            "subscribed": subscribed,
            "peer_id": peer_id,
            "target_peer_id": target_peer_id
        })
    
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def get_subscription_status(request: Request) -> Response:
    """Get current subscription status for a peer."""
    peer_id = request.path_params.get("peer_id")
    
    if not peer_id:
        return JSONResponse({"error": "peer_id is required"}, status_code=400)
    
    session = room_service.get_peer_session(peer_id)
    
    if not session:
        return JSONResponse({"error": "Peer not found"}, status_code=404)
    
    return JSONResponse({
        "peer_id": peer_id,
        "subscribed_peers": list(session.subscribed_peers)
    })


async def health_check(request: Request) -> Response:
    """Health check endpoint."""
    return JSONResponse({"status": "OK"})


async def serve_index(request: Request) -> Response:
    """Serve the main HTML interface."""
    return templates.TemplateResponse("index.html", {"request": request})


# Define routes
routes = [
    Route("/", serve_index, methods=["GET"]),
    Route("/health", health_check, methods=["GET"]),
    Route("/api/peers", create_peer, methods=["POST"]),
    Route("/api/rooms/{room_name}/peers", get_available_peers, methods=["GET"]),
    Route("/api/subscriptions", toggle_subscription, methods=["POST"]),
    Route("/api/peers/{peer_id}/subscriptions", get_subscription_status, methods=["GET"]),
]

# Define middleware
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

# Create application
app = Starlette(
    routes=routes,
    middleware=middleware,
)