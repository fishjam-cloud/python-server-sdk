from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dial_config import DialConfig
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    room_id: str,
    component_id: str,
    *,
    json_body: DialConfig,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/sip/{room_id}/{component_id}/call".format(
            room_id=room_id,
            component_id=component_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = Error.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    room_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DialConfig,
) -> Response[Union[Any, Error]]:
    """Make a call from the SIP component to the provided phone number

    Args:
        room_id (str):
        component_id (str):
        json_body (DialConfig): Dial config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        component_id=component_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    room_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DialConfig,
) -> Optional[Union[Any, Error]]:
    """Make a call from the SIP component to the provided phone number

    Args:
        room_id (str):
        component_id (str):
        json_body (DialConfig): Dial config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
    """

    return sync_detailed(
        room_id=room_id,
        component_id=component_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DialConfig,
) -> Response[Union[Any, Error]]:
    """Make a call from the SIP component to the provided phone number

    Args:
        room_id (str):
        component_id (str):
        json_body (DialConfig): Dial config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        component_id=component_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DialConfig,
) -> Optional[Union[Any, Error]]:
    """Make a call from the SIP component to the provided phone number

    Args:
        room_id (str):
        component_id (str):
        json_body (DialConfig): Dial config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            component_id=component_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
