from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.viewer_details_response import ViewerDetailsResponse
from ...types import Response


def _get_kwargs(
    stream_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/livestream/{stream_id}/viewer".format(
            stream_id=stream_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ViewerDetailsResponse]]:
    if response.status_code == 201:
        response_201 = ViewerDetailsResponse.from_dict(response.json())

        return response_201
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, ViewerDetailsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    stream_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, ViewerDetailsResponse]]:
    """Creates viewer

    Args:
        stream_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ViewerDetailsResponse]]
    """

    kwargs = _get_kwargs(
        stream_id=stream_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stream_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, ViewerDetailsResponse]]:
    """Creates viewer

    Args:
        stream_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ViewerDetailsResponse]
    """

    return sync_detailed(
        stream_id=stream_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    stream_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, ViewerDetailsResponse]]:
    """Creates viewer

    Args:
        stream_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ViewerDetailsResponse]]
    """

    kwargs = _get_kwargs(
        stream_id=stream_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stream_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, ViewerDetailsResponse]]:
    """Creates viewer

    Args:
        stream_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ViewerDetailsResponse]
    """

    return (
        await asyncio_detailed(
            stream_id=stream_id,
            client=client,
        )
    ).parsed
