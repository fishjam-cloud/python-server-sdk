from contextlib import asynccontextmanager

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

from .composition_service import CompositionService
from .config import COMPOSITION_URL, FISHJAM_ID, FISHJAM_TOKEN
from .fishjam_service import FishjamService


def clean_up(*services) -> None:
    for service in services:
        if service is None:
            continue

        try:
            service.cleanup()
        except Exception as error:
            print(f"cleanup failed: {error}")


@asynccontextmanager
async def lifespan(app: Starlette):
    fishjam = composition = None

    try:
        fishjam = FishjamService(FISHJAM_ID, FISHJAM_TOKEN)
        composition = CompositionService(FISHJAM_TOKEN, COMPOSITION_URL)
        composition.register_assets()
        composition.play_movie()
        composition.camera()
        composition.stream_to(
            fishjam.livestream_whip_url(), fishjam.create_streamer_token()
        )
    except Exception:
        clean_up(composition, fishjam)
        raise

    app.state.fishjam = fishjam
    app.state.composition = composition

    try:
        yield
    finally:
        clean_up(composition, fishjam)
        print("deleted the composition and the livestream room")


async def streamer(request: Request) -> Response:
    camera = request.app.state.composition.camera()

    return JSONResponse({"url": camera.url, "token": camera.bearer_token})


async def viewer(request: Request) -> Response:
    fishjam = request.app.state.fishjam

    return JSONResponse({
        "url": fishjam.livestream_whep_url(),
        "token": fishjam.create_viewer_token(),
    })


app = Starlette(
    lifespan=lifespan,
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
