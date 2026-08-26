from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

from .composition_service import CompositionService
from .config import COMPOSITION_URL, FISHJAM_ID, FISHJAM_TOKEN
from .fishjam_service import FishjamService

fishjam = FishjamService(FISHJAM_ID, FISHJAM_TOKEN)
composition = CompositionService(FISHJAM_TOKEN, COMPOSITION_URL)


def start_composing() -> None:
    composition.register_assets()
    composition.play_movie()
    composition.camera()
    composition.stream_to(
        fishjam.livestream_whip_url(), fishjam.create_streamer_token()
    )


def cleanup() -> None:
    for service in (composition, fishjam):
        try:
            service.cleanup()
        except Exception as error:
            print(f"cleanup failed: {error}")


async def streamer(_request: Request) -> Response:
    camera = composition.camera()

    return JSONResponse({"url": camera.url, "token": camera.bearer_token})


async def viewer(_request: Request) -> Response:
    return JSONResponse({
        "url": fishjam.livestream_whep_url(),
        "token": fishjam.create_viewer_token(),
    })


app = Starlette(
    routes=[
        Route("/streamer", streamer, methods=["GET"]),
        Route("/viewer", viewer, methods=["GET"]),
    ],
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ],
)
