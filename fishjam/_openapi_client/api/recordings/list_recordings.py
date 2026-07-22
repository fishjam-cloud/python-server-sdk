from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_recordings_metadata import ListRecordingsMetadata
from ...models.recording_list_response import RecordingListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    metadata: ListRecordingsMetadata | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_metadata: dict[str, Any] | Unset = UNSET
    if not isinstance(metadata, Unset):
        json_metadata = metadata.to_dict()
    if not isinstance(json_metadata, Unset):
        params.update(json_metadata)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/recordings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | RecordingListResponse | None:
    if response.status_code == 200:
        response_200 = RecordingListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | RecordingListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    metadata: ListRecordingsMetadata | Unset = UNSET,
) -> Response[Error | RecordingListResponse]:
    """List recordings

     List recordings for the tenant, optionally filtered by metadata.

    Args:
        metadata (ListRecordingsMetadata | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RecordingListResponse]
    """

    kwargs = _get_kwargs(
        metadata=metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    metadata: ListRecordingsMetadata | Unset = UNSET,
) -> Error | RecordingListResponse | None:
    """List recordings

     List recordings for the tenant, optionally filtered by metadata.

    Args:
        metadata (ListRecordingsMetadata | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RecordingListResponse
    """

    return sync_detailed(
        client=client,
        metadata=metadata,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    metadata: ListRecordingsMetadata | Unset = UNSET,
) -> Response[Error | RecordingListResponse]:
    """List recordings

     List recordings for the tenant, optionally filtered by metadata.

    Args:
        metadata (ListRecordingsMetadata | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RecordingListResponse]
    """

    kwargs = _get_kwargs(
        metadata=metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    metadata: ListRecordingsMetadata | Unset = UNSET,
) -> Error | RecordingListResponse | None:
    """List recordings

     List recordings for the tenant, optionally filtered by metadata.

    Args:
        metadata (ListRecordingsMetadata | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RecordingListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            metadata=metadata,
        )
    ).parsed
