# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods, missing-module-docstring

import asyncio
import socket
import time
from multiprocessing import Process, Queue

import pytest
import requests
import websockets

from fishjam import FishjamClient, FishjamNotifier, RoomOptions
from fishjam.events import (
    ServerMessagePeerAdded,
    ServerMessagePeerConnected,
    ServerMessagePeerDeleted,
    ServerMessagePeerDisconnected,
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
)
from tests.support.asyncio_utils import assert_events
from tests.support.env import (
    FISHJAM_ID,
    FISHJAM_MANAGEMENT_TOKEN,
    WEBHOOK_SERVER_URL,
    WEBHOOK_URL,
)
from tests.support.peer_socket import PeerSocket
from tests.support.webhook_notifier import run_server

queue = Queue()


@pytest.fixture(scope="session", autouse=True)
def start_server():
    flask_process = Process(target=run_server, args=(queue,))
    flask_process.start()

    timeout = 60  # wait maximum of 60 seconds
    while True:
        try:
            response = requests.get(WEBHOOK_SERVER_URL, timeout=1_000)
            if response.status_code == 200:  # Or another condition
                break
        except (requests.ConnectionError, socket.error):
            time.sleep(1)  # wait for 1 second before trying again
            timeout -= 1
            if timeout == 0:
                pytest.fail("Server did not start in the expected time")

    yield  # This is where the testing happens.

    flask_process.terminate()


class TestConnectingToServer:
    @pytest.mark.asyncio
    async def test_valid_credentials(self):
        notifier = FishjamNotifier(
            fishjam_id=FISHJAM_ID,
            management_token=FISHJAM_MANAGEMENT_TOKEN,
        )

        @notifier.on_server_notification
        def handle_notitifcation(_notification):
            pass

        async with asyncio.TaskGroup() as tg:
            tg.create_task(notifier.connect())
            await notifier.wait_ready()

            assert (
                notifier._websocket
                and notifier._websocket.state == websockets.State.OPEN
            )


@pytest.fixture
def room_api():
    return FishjamClient(FISHJAM_ID, FISHJAM_MANAGEMENT_TOKEN)


@pytest.fixture
def notifier():
    notifier = FishjamNotifier(
        fishjam_id=FISHJAM_ID,
        management_token=FISHJAM_MANAGEMENT_TOKEN,
    )

    return notifier


class TestReceivingNotifications:
    @pytest.mark.asyncio
    async def test_room_created_deleted(
        self, room_api: FishjamClient, notifier: FishjamNotifier
    ):
        event_checks = [ServerMessageRoomCreated, ServerMessageRoomDeleted]

        async with asyncio.TaskGroup() as tg:
            assert_task = tg.create_task(assert_events(notifier, event_checks.copy()))

            tg.create_task(notifier.connect())
            await notifier.wait_ready()

            options = RoomOptions(webhook_url=WEBHOOK_URL)
            room = room_api.create_room(options=options)

            room_api.delete_room(room.id)

            await assert_task

        for event in event_checks:
            self.assert_event(event)

    @pytest.mark.asyncio
    async def test_peer_connected_disconnected(
        self, room_api: FishjamClient, notifier: FishjamNotifier
    ):
        event_checks = [
            ServerMessageRoomCreated,
            ServerMessagePeerAdded,
            ServerMessagePeerConnected,
            ServerMessagePeerDisconnected,
            ServerMessagePeerDeleted,
            ServerMessageRoomDeleted,
        ]

        async with asyncio.TaskGroup() as tg:
            assert_task = tg.create_task(assert_events(notifier, event_checks.copy()))

            tg.create_task(notifier.connect())
            await notifier.wait_ready()

            options = RoomOptions(webhook_url=WEBHOOK_URL)
            room = room_api.create_room(options=options)

            peer, token = room_api.create_peer(room.id)
            peer_socket = PeerSocket(fishjam_url=FISHJAM_ID)
            tg.create_task(peer_socket.connect(token))

            await peer_socket.wait_ready()

            room_api.delete_peer(room.id, peer.id)
            room_api.delete_room(room.id)

            await assert_task

        for event in event_checks:
            self.assert_event(event)

    @pytest.mark.asyncio
    async def test_peer_connected_room_deleted(
        self, room_api: FishjamClient, notifier: FishjamNotifier
    ):
        event_checks = [
            ServerMessageRoomCreated,
            ServerMessagePeerAdded,
            ServerMessagePeerConnected,
            ServerMessagePeerDeleted,
            ServerMessageRoomDeleted,
        ]

        async with asyncio.TaskGroup() as tg:
            assert_task = tg.create_task(assert_events(notifier, event_checks.copy()))

            tg.create_task(notifier.connect())
            await notifier.wait_ready()

            options = RoomOptions(webhook_url=WEBHOOK_URL)
            room = room_api.create_room(options=options)
            _peer, token = room_api.create_peer(room.id)

            peer_socket = PeerSocket(fishjam_url=FISHJAM_ID)
            tg.create_task(peer_socket.connect(token))

            await peer_socket.wait_ready()

            room_api.delete_room(room.id)

            await assert_task

        for event in event_checks:
            self.assert_event(event)

    def assert_event(self, event):
        data = queue.get(timeout=2.5)
        assert data == event or isinstance(data, event)
