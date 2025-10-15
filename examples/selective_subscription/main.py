from contextlib import asynccontextmanager

import uvicorn

from selective_subscription.app import app, room_service
from selective_subscription.config import HOST, PORT
from selective_subscription.notification_handler import NotificationHandler
from selective_subscription.worker import async_worker


@asynccontextmanager
async def lifespan(app):
    async with async_worker() as worker:
        notification_handler = NotificationHandler(room_service)
        worker.run_in_background(notification_handler.start())
        print(f"Selective subscription demo started on http://{HOST}:{PORT}")
        yield


app.router.lifespan_context = lifespan


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True, log_level="info")
