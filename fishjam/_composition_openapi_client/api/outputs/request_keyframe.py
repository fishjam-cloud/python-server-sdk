from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.empty_response import EmptyResponse
from ...types import Response


def _get_kwargs(
    composition_id: str,
    output_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/composition/{composition_id}/output/{output_id}/request_keyframe".format(
            composition_id=quote(str(composition_id), safe=""),
            output_id=quote(str(output_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | EmptyResponse | None:
    if response.status_code == 200:
        response_200 = EmptyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ApiError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | EmptyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    composition_id: str,
    output_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | EmptyResponse]:
    """Request a keyframe

    Args:
        composition_id (str):
        output_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | EmptyResponse]
    """

    kwargs = _get_kwargs(
        composition_id=composition_id,
        output_id=output_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    composition_id: str,
    output_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | EmptyResponse | None:
    """Request a keyframe

    Args:
        composition_id (str):
        output_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | EmptyResponse
    """

    return sync_detailed(
        composition_id=composition_id,
        output_id=output_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    composition_id: str,
    output_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | EmptyResponse]:
    """Request a keyframe

    Args:
        composition_id (str):
        output_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | EmptyResponse]
    """

    kwargs = _get_kwargs(
        composition_id=composition_id,
        output_id=output_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    composition_id: str,
    output_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | EmptyResponse | None:
    """Request a keyframe

    Args:
        composition_id (str):
        output_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | EmptyResponse
    """

    return (
        await asyncio_detailed(
            composition_id=composition_id,
            output_id=output_id,
            client=client,
        )
    ).parsed
