import sys
from contextlib import asynccontextmanager

import uvicorn
from composition.app import app, cleanup, start_composing
from composition.config import HOST, PORT


@asynccontextmanager
async def lifespan(_app):
    try:
        start_composing()
    except Exception as error:
        print(f"failed to start composing: {error}", file=sys.stderr)
        cleanup()
        raise SystemExit(1) from error

    print(f"streamer credentials on http://{HOST}:{PORT}/streamer")
    print(f"viewer token on http://{HOST}:{PORT}/viewer")

    try:
        yield
    finally:
        cleanup()
        print("deleted the composition and the livestream room")


app.router.lifespan_context = lifespan


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT, log_level="info")
