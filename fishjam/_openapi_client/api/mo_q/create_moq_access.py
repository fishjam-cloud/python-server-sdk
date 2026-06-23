from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.moq_access import MoqAccess
from ...models.moq_access_config import MoqAccessConfig
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MoqAccessConfig | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/moq/access",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MoqAccess | None:
    if response.status_code == 200:
        response_200 = MoqAccess.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | MoqAccess]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MoqAccessConfig | Unset = UNSET,
) -> Response[Error | MoqAccess]:
    """Create MoQ access

     Issue a short-lived JWT for a Media over QUIC client.

    Args:
        body (MoqAccessConfig | Unset): MoQ access configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MoqAccess]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: MoqAccessConfig | Unset = UNSET,
) -> Error | MoqAccess | None:
    """Create MoQ access

     Issue a short-lived JWT for a Media over QUIC client.

    Args:
        body (MoqAccessConfig | Unset): MoQ access configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MoqAccess
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MoqAccessConfig | Unset = UNSET,
) -> Response[Error | MoqAccess]:
    """Create MoQ access

     Issue a short-lived JWT for a Media over QUIC client.

    Args:
        body (MoqAccessConfig | Unset): MoQ access configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MoqAccess]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MoqAccessConfig | Unset = UNSET,
) -> Error | MoqAccess | None:
    """Create MoQ access

     Issue a short-lived JWT for a Media over QUIC client.

    Args:
        body (MoqAccessConfig | Unset): MoQ access configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MoqAccess
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
