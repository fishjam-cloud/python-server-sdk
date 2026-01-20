import pytest

from fishjam._openapi_client.client import AuthenticatedClient
from fishjam.version import get_version


def test_authenticated_client_sets_sdk_and_auth_headers_sync():
    client = AuthenticatedClient(
        base_url="https://example.com",
        token="token123",
        headers={"custom": "value"},
    )

    httpx_client = client.get_httpx_client()
    try:
        headers = httpx_client.headers

        assert headers[client.auth_header_name] == "Bearer token123"
        assert headers[client.api_header_name] == f"{client.api_prefix}-{get_version()}"
        assert headers["custom"] == "value"
    finally:
        httpx_client.close()


@pytest.mark.asyncio
async def test_authenticated_client_sets_sdk_and_auth_headers_async():
    client = AuthenticatedClient(
        base_url="https://example.com",
        token="token456",
        headers={"another": "header"},
    )

    async_client = client.get_async_httpx_client()
    try:
        headers = async_client.headers

        assert headers[client.auth_header_name] == "Bearer token456"
        assert headers[client.api_header_name] == f"{client.api_prefix}-{get_version()}"
        assert headers["another"] == "header"
    finally:
        await async_client.aclose()
