import pytest

from fishjam import decode_server_notifications, receive_binary
from fishjam.events import (
    ServerMessagePeerConnected,
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
)
from fishjam.events._protos.fishjam import (
    ServerMessage,
    ServerMessageAuthRequest,
    ServerMessageNotificationBatch,
)


def test_single_notification_is_returned_unwrapped():
    binary = bytes(ServerMessage(room_created=ServerMessageRoomCreated(room_id="r1")))

    result = receive_binary(binary)

    assert isinstance(result, ServerMessageRoomCreated)
    assert result.room_id == "r1"


def test_unsupported_single_message_returns_none():
    binary = bytes(ServerMessage(auth_request=ServerMessageAuthRequest(token="t")))

    assert receive_binary(binary) is None


def test_batch_is_unpacked_into_ordered_list():
    binary = bytes(
        ServerMessage(
            notification_batch=ServerMessageNotificationBatch(
                notifications=[
                    ServerMessage(room_created=ServerMessageRoomCreated(room_id="r1")),
                    ServerMessage(
                        peer_connected=ServerMessagePeerConnected(
                            room_id="r1", peer_id="p1"
                        )
                    ),
                    ServerMessage(room_deleted=ServerMessageRoomDeleted(room_id="r1")),
                ]
            )
        )
    )

    result = receive_binary(binary)

    assert isinstance(result, list)
    assert [type(n) for n in result] == [
        ServerMessageRoomCreated,
        ServerMessagePeerConnected,
        ServerMessageRoomDeleted,
    ]
    assert result[0].room_id == "r1"
    assert result[1].peer_id == "p1"


def test_batch_filters_out_unsupported_members():
    binary = bytes(
        ServerMessage(
            notification_batch=ServerMessageNotificationBatch(
                notifications=[
                    ServerMessage(room_created=ServerMessageRoomCreated(room_id="r1")),
                    ServerMessage(auth_request=ServerMessageAuthRequest(token="t")),
                    ServerMessage(room_deleted=ServerMessageRoomDeleted(room_id="r1")),
                ]
            )
        )
    )

    result = receive_binary(binary)

    assert isinstance(result, list)
    assert [type(n) for n in result] == [
        ServerMessageRoomCreated,
        ServerMessageRoomDeleted,
    ]


def test_empty_batch_returns_empty_list():
    binary = bytes(
        ServerMessage(
            notification_batch=ServerMessageNotificationBatch(notifications=[])
        )
    )

    result = receive_binary(binary)

    assert result == []


def test_receive_binary_is_deprecated():
    binary = bytes(ServerMessage(room_created=ServerMessageRoomCreated(room_id="r1")))

    with pytest.warns(DeprecationWarning):
        receive_binary(binary)


def test_decode_single_notification_returns_one_element_list():
    binary = bytes(ServerMessage(room_created=ServerMessageRoomCreated(room_id="r1")))

    result = decode_server_notifications(binary)

    assert isinstance(result, list)
    assert [type(n) for n in result] == [ServerMessageRoomCreated]
    assert result[0].room_id == "r1"


def test_decode_unsupported_single_message_returns_empty_list():
    binary = bytes(ServerMessage(auth_request=ServerMessageAuthRequest(token="t")))

    assert decode_server_notifications(binary) == []


def test_decode_batch_is_unpacked_into_ordered_list():
    binary = bytes(
        ServerMessage(
            notification_batch=ServerMessageNotificationBatch(
                notifications=[
                    ServerMessage(room_created=ServerMessageRoomCreated(room_id="r1")),
                    ServerMessage(
                        peer_connected=ServerMessagePeerConnected(
                            room_id="r1", peer_id="p1"
                        )
                    ),
                    ServerMessage(room_deleted=ServerMessageRoomDeleted(room_id="r1")),
                ]
            )
        )
    )

    result = decode_server_notifications(binary)

    assert [type(n) for n in result] == [
        ServerMessageRoomCreated,
        ServerMessagePeerConnected,
        ServerMessageRoomDeleted,
    ]
    assert result[0].room_id == "r1"
    assert result[1].peer_id == "p1"


def test_decode_batch_filters_out_unsupported_members():
    binary = bytes(
        ServerMessage(
            notification_batch=ServerMessageNotificationBatch(
                notifications=[
                    ServerMessage(room_created=ServerMessageRoomCreated(room_id="r1")),
                    ServerMessage(auth_request=ServerMessageAuthRequest(token="t")),
                    ServerMessage(room_deleted=ServerMessageRoomDeleted(room_id="r1")),
                ]
            )
        )
    )

    result = decode_server_notifications(binary)

    assert [type(n) for n in result] == [
        ServerMessageRoomCreated,
        ServerMessageRoomDeleted,
    ]


def test_decode_empty_batch_returns_empty_list():
    binary = bytes(
        ServerMessage(
            notification_batch=ServerMessageNotificationBatch(notifications=[])
        )
    )

    assert decode_server_notifications(binary) == []
