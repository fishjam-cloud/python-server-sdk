from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.empty_response import EmptyResponse
from ...models.unregister_renderer import UnregisterRenderer
from ...types import Response


def _get_kwargs(
    composition_id: str,
    image_id: str,
    *,
    body: UnregisterRenderer,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/composition/{composition_id}/image/{image_id}/unregister".format(
            composition_id=quote(str(composition_id), safe=""),
            image_id=quote(str(image_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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

    if response.status_code == 422:
        response_422 = ApiError.from_dict(response.json())

        return response_422

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
    image_id: str,
    *,
    client: AuthenticatedClient,
    body: UnregisterRenderer,
) -> Response[ApiError | EmptyResponse]:
    """Unregister an image

    Args:
        composition_id (str):
        image_id (str):
        body (UnregisterRenderer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | EmptyResponse]
    """

    kwargs = _get_kwargs(
        composition_id=composition_id,
        image_id=image_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    composition_id: str,
    image_id: str,
    *,
    client: AuthenticatedClient,
    body: UnregisterRenderer,
) -> ApiError | EmptyResponse | None:
    """Unregister an image

    Args:
        composition_id (str):
        image_id (str):
        body (UnregisterRenderer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | EmptyResponse
    """

    return sync_detailed(
        composition_id=composition_id,
        image_id=image_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    composition_id: str,
    image_id: str,
    *,
    client: AuthenticatedClient,
    body: UnregisterRenderer,
) -> Response[ApiError | EmptyResponse]:
    """Unregister an image

    Args:
        composition_id (str):
        image_id (str):
        body (UnregisterRenderer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | EmptyResponse]
    """

    kwargs = _get_kwargs(
        composition_id=composition_id,
        image_id=image_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    composition_id: str,
    image_id: str,
    *,
    client: AuthenticatedClient,
    body: UnregisterRenderer,
) -> ApiError | EmptyResponse | None:
    """Unregister an image

    Args:
        composition_id (str):
        image_id (str):
        body (UnregisterRenderer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | EmptyResponse
    """

    return (
        await asyncio_detailed(
            composition_id=composition_id,
            image_id=image_id,
            client=client,
            body=body,
        )
    ).parsed
