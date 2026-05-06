# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods, missing-module-docstring

import asyncio

from fishjam import FishjamNotifier

ASSERTION_TIMEOUT = 15.0


async def assert_events(
    notifier: FishjamNotifier,
    event_checks: list,
    *,
    room_id_future: asyncio.Future | None = None,
):
    await _assert_messages(
        notifier.on_server_notification, event_checks, room_id_future
    )


async def _assert_messages(notifier_callback, message_checks, room_id_future):
    success_event = asyncio.Event()
    pending: list = []
    room_id_holder: dict = {"value": None, "set": False}

    def _consume(message):
        if len(message_checks) > 0:
            expected_msg = message_checks[0]
            if message == expected_msg or isinstance(message, expected_msg):
                message_checks.pop(0)
        if message_checks == []:
            success_event.set()

    @notifier_callback
    def handle_message(message):
        if not room_id_holder["set"]:
            pending.append(message)
            return

        expected_room_id = room_id_holder["value"]
        if expected_room_id is not None:
            if getattr(message, "room_id", None) != expected_room_id:
                return

        _consume(message)

    async def _wait_for_success():
        if room_id_future is not None:
            room_id_holder["value"] = await room_id_future
        room_id_holder["set"] = True
        for msg in pending:
            handle_message(msg)
        pending.clear()
        await success_event.wait()

    try:
        await asyncio.wait_for(_wait_for_success(), ASSERTION_TIMEOUT)
    except asyncio.exceptions.TimeoutError as exc:
        raise asyncio.exceptions.TimeoutError(
            f"{message_checks[0]} hasn't been received within timeout"
        ) from exc
