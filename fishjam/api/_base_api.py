from fishjam._openapi_client.client import AuthenticatedClient
from fishjam._openapi_client.models import Error
from fishjam._openapi_client.types import Response
from fishjam.errors import HTTPError


class BaseApi:
    def __init__(self, fishjam_url: str, management_token: str):
        self.client = AuthenticatedClient(f"{fishjam_url}", token=management_token)

    def _request(self, method, **kwargs):
        response: Response = method.sync_detailed(client=self.client, **kwargs)

        if isinstance(response.parsed, Error):
            raise HTTPError.from_response(response)

        return response.parsed
