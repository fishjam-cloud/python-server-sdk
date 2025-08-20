import asyncio
import os

import pytest

from fishjam import FishjamClient, FishjamNotifier
from fishjam.agent.agent import Agent
from fishjam.agent.errors import AgentAuthError
from fishjam.api._fishjam_client import Room
from fishjam.events import (
    ServerMessagePeerConnected,
)
from fishjam.events.allowed_notifications import AllowedNotification

HOST = "fishjam" if os.getenv("DOCKER_TEST") == "TRUE" else "localhost"
FISHJAM_URL = f"http://{HOST}:5002"
FISHJAM_ID = ""
SERVER_API_TOKEN = "development"


@pytest.fixture
def room_api():
    return FishjamClient(FISHJAM_ID, SERVER_API_TOKEN, fishjam_url=FISHJAM_URL)


@pytest.fixture
def room(room_api: FishjamClient):
    room = room_api.create_room()
    yield room
    room_api.delete_room(room.id)


@pytest.fixture
def agent(room: Room, room_api: FishjamClient):
    agent = room_api.create_agent(room.id)
    yield agent
    room_api.delete_peer(room.id, agent.id)


@pytest.fixture
def notifier():
    notifier = FishjamNotifier(
        fishjam_id=FISHJAM_ID,
        management_token=SERVER_API_TOKEN,
        fishjam_url=FISHJAM_URL,
    )

    return notifier


class TestAgentApi:
    def test_create_delete_agent(self, room_api: FishjamClient, room: Room):
        agent = room_api.create_agent(room.id)
        room = room_api.get_room(room.id)

        assert len(room.peers) == 1
        assert room.peers[0].id == agent.id
        assert room.peers[0].type == "agent"
        assert room.peers[0].status == "disconnected"

        room_api.delete_peer(room.id, agent.id)

        room = room_api.get_room(room.id)

        assert room.peers == []


async def wait_event(event: asyncio.Event, timeout: float = 5):
    await asyncio.wait_for(event.wait(), timeout)


class TestAgentConnection:
    @pytest.mark.asyncio
    async def test_connect_disconnect(
        self,
        room_api: FishjamClient,
        room: Room,
        agent: Agent,
        notifier: FishjamNotifier,
    ):
        connect_event = asyncio.Event()
        disconnect_event = asyncio.Event()

        @notifier.on_server_notification
        def _(notification: AllowedNotification):
            print(f"Received notification {notification}")
            if (
                isinstance(notification, ServerMessagePeerConnected)
                and notification.peer_id == agent.id
            ):
                connect_event.set()
                disconnect_event.set()

        await agent.connect()
        await wait_event(connect_event)

        room = room_api.get_room(room.id)
        assert len(room.peers) == 1
        assert room.peers[0].id == agent.id
        assert room.peers[0].status == "connected"

        await agent.disconnect()
        await wait_event(disconnect_event)

    @pytest.mark.asyncio
    async def test_invalid_auth(self, room_api: FishjamClient):
        agent = Agent("fake-id", "fake-token", room_api._fishjam_url)

        with pytest.raises(AgentAuthError):
            await agent.connect()

        with pytest.raises(AgentAuthError):
            async with agent:
                pass

    @pytest.mark.asyncio
    async def test_context_manager(
        self,
        room_api: FishjamClient,
        room: Room,
        agent: Agent,
        notifier: FishjamNotifier,
    ):
        connect_event = asyncio.Event()
        disconnect_event = asyncio.Event()

        @notifier.on_server_notification
        def _(notification: AllowedNotification):
            print(f"Received notification {notification}")
            if (
                isinstance(notification, ServerMessagePeerConnected)
                and notification.peer_id == agent.id
            ):
                connect_event.set()
                disconnect_event.set()

        async with agent:
            await wait_event(connect_event)

            room = room_api.get_room(room.id)
            assert len(room.peers) == 1
            assert room.peers[0].id == agent.id
            assert room.peers[0].status == "connected"

        await wait_event(disconnect_event)
