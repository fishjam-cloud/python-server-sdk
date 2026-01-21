from typing import cast

from fishjam._openapi_client.client import AuthenticatedClient
from fishjam._openapi_client.models import Error
from fishjam._openapi_client.types import Response
from fishjam.errors import HTTPError
from fishjam.utils import get_fishjam_url
from fishjam.version import get_version


class Client:
    def __init__(self, fishjam_id: str, management_token: str):
        self._fishjam_url = get_fishjam_url(fishjam_id)
        self.client = AuthenticatedClient(
            self._fishjam_url,
            token=management_token,
            headers={"x-fishjam-api-client": f"python-server/{get_version()}"},
        )

    def _request(self, method, **kwargs):
        response = method.sync_detailed(client=self.client, **kwargs)

        if isinstance(response.parsed, Error):
            response = cast(Response[Error], response)
            raise HTTPError.from_response(response)

        return response.parsed
