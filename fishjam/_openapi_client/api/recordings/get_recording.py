from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.recording_details_response import RecordingDetailsResponse
from ...types import Response


def _get_kwargs(
    recording_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/recordings/{recording_id}".format(
            recording_id=quote(str(recording_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | RecordingDetailsResponse | None:
    if response.status_code == 200:
        response_200 = RecordingDetailsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | RecordingDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    recording_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | RecordingDetailsResponse]:
    """Get a recording

     Get a recording by id.

    Args:
        recording_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RecordingDetailsResponse]
    """

    kwargs = _get_kwargs(
        recording_id=recording_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    recording_id: str,
    *,
    client: AuthenticatedClient,
) -> Error | RecordingDetailsResponse | None:
    """Get a recording

     Get a recording by id.

    Args:
        recording_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RecordingDetailsResponse
    """

    return sync_detailed(
        recording_id=recording_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    recording_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | RecordingDetailsResponse]:
    """Get a recording

     Get a recording by id.

    Args:
        recording_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RecordingDetailsResponse]
    """

    kwargs = _get_kwargs(
        recording_id=recording_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    recording_id: str,
    *,
    client: AuthenticatedClient,
) -> Error | RecordingDetailsResponse | None:
    """Get a recording

     Get a recording by id.

    Args:
        recording_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RecordingDetailsResponse
    """

    return (
        await asyncio_detailed(
            recording_id=recording_id,
            client=client,
        )
    ).parsed
