"""
Notifier listening to WebSocket events
"""

import asyncio
from typing import Any, Callable

import betterproto
from websockets import client
from websockets.exceptions import ConnectionClosed

from fishjam.events import (
    ServerMessagePeerAdded,
    ServerMessagePeerConnected,
    ServerMessagePeerCrashed,
    ServerMessagePeerDeleted,
    ServerMessagePeerDisconnected,
    ServerMessagePeerMetadataUpdated,
    ServerMessageRoomCrashed,
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
    ServerMessageTrackAdded,
    ServerMessageTrackMetadataUpdated,
    ServerMessageTrackRemoved,
)
from fishjam.events._protos.fishjam import (
    ServerMessage,
    ServerMessageAuthenticated,
    ServerMessageAuthRequest,
    ServerMessageEventType,
    ServerMessageSubscribeRequest,
    ServerMessageSubscribeResponse,
)

ALLOWED_NOTIFICATION = (
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
    ServerMessageRoomCrashed,
    ServerMessagePeerAdded,
    ServerMessagePeerDeleted,
    ServerMessagePeerConnected,
    ServerMessagePeerDisconnected,
    ServerMessagePeerMetadataUpdated,
    ServerMessagePeerCrashed,
    ServerMessageTrackAdded,
    ServerMessageTrackRemoved,
    ServerMessageTrackMetadataUpdated,
)


class FishjamNotifier:
    """
    Allows for receiving WebSocket messages from Fishjam.
    """

    def __init__(self, fishjam_url: str, management_token: str):
        """
        Create FishjamNotifier instance, providing the fishjam url and management token.
        """

        self._fishjam_url = (
            f"{fishjam_url.replace('http', 'ws')}/socket/server/websocket"
        )
        self._management_token = management_token
        self._websocket = None
        self._ready = False

        self._ready_event: asyncio.Event = None

        self._notification_handler: Callable = None

    def on_server_notification(self, handler: Callable[[Any], None]):
        """
        Decorator used for defining handler for Fishjam Notifications
        """
        self._notification_handler = handler
        return handler

    async def connect(self):
        """
        A coroutine which connects FishjamNotifier to Fishjam and listens for
        all incoming messages from the Fishjam.

        It runs until the connection isn't closed.

        The incoming messages are handled by the functions defined using the
        `on_server_notification` decorator.

        The handler have to be defined before calling `connect`,
        otherwise the messages won't be received.
        """
        async with client.connect(self._fishjam_url) as websocket:
            try:
                self._websocket = websocket
                await self._authenticate()

                if self._notification_handler:
                    await self._subscribe_event(
                        event=ServerMessageEventType.EVENT_TYPE_SERVER_NOTIFICATION
                    )

                self._ready = True
                if self._ready_event:
                    self._ready_event.set()

                await self._receive_loop()
            finally:
                self._websocket = None

    async def wait_ready(self) -> True:
        """
        Waits until the notifier is connected and authenticated to Fishjam.

        If already connected, returns `True` immediately.
        """
        if self._ready:
            return True

        if self._ready_event is None:
            self._ready_event = asyncio.Event()

        await self._ready_event.wait()

    async def _authenticate(self):
        msg = ServerMessage(
            auth_request=ServerMessageAuthRequest(token=self._management_token)
        )
        await self._websocket.send(bytes(msg))

        try:
            message = await self._websocket.recv()
        except ConnectionClosed as exception:
            if "invalid token" in str(exception):
                raise RuntimeError("Invalid server_api_token") from exception
            raise

        message = ServerMessage().parse(message)

        _type, message = betterproto.which_one_of(message, "content")
        assert isinstance(message, ServerMessageAuthenticated)

    async def _receive_loop(self):
        while True:
            message = await self._websocket.recv()
            message = ServerMessage().parse(message)
            _which, message = betterproto.which_one_of(message, "content")

            if isinstance(message, ALLOWED_NOTIFICATION):
                self._notification_handler(message)

    async def _subscribe_event(self, event: ServerMessageEventType):
        request = ServerMessage(subscribe_request=ServerMessageSubscribeRequest(event))

        await self._websocket.send(bytes(request))
        message = await self._websocket.recv()
        message = ServerMessage().parse(message)
        _which, message = betterproto.which_one_of(message, "content")
        assert isinstance(message, ServerMessageSubscribeResponse)
