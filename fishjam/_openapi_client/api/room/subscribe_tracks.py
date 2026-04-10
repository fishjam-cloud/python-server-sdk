from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.subscribe_tracks_body import SubscribeTracksBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    room_id: str,
    id: str,
    *,
    body: SubscribeTracksBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/room/{room_id}/peer/{id}/subscribe_tracks".format(
            room_id=quote(str(room_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    room_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: SubscribeTracksBody | Unset = UNSET,
) -> Response[Any | Error]:
    """Subscribe peer to specific tracks

    Args:
        room_id (str):
        id (str):
        body (SubscribeTracksBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    room_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: SubscribeTracksBody | Unset = UNSET,
) -> Any | Error | None:
    """Subscribe peer to specific tracks

    Args:
        room_id (str):
        id (str):
        body (SubscribeTracksBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        room_id=room_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: SubscribeTracksBody | Unset = UNSET,
) -> Response[Any | Error]:
    """Subscribe peer to specific tracks

    Args:
        room_id (str):
        id (str):
        body (SubscribeTracksBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: SubscribeTracksBody | Unset = UNSET,
) -> Any | Error | None:
    """Subscribe peer to specific tracks

    Args:
        room_id (str):
        id (str):
        body (SubscribeTracksBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
