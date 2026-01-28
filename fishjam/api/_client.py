import json
import warnings
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
        self.warnings_shown = False

    def _request(self, method, **kwargs):
        response = method.sync_detailed(client=self.client, **kwargs)
        self._handle_deprecation_header(response.headers)

        if isinstance(response.parsed, Error):
            response = cast(Response[Error], response)
            raise HTTPError.from_response(response)

        return response.parsed

    def _handle_deprecation_header(self, headers):
        deprecation_warning = headers.get("x-fishjam-api-deprecated")
        if deprecation_warning and not self.warnings_shown:
            self.warnings_shown = True
            try:
                deprecation_data = json.loads(deprecation_warning)
            except (json.JSONDecodeError, TypeError, ValueError):
                return

            status = deprecation_data["status"]
            msg = deprecation_data["message"]

            if not status or not msg:
                return

            match status:
                case "unsupported":
                    warnings.warn(message=msg, category=UserWarning, stacklevel=4)
                case "deprecated":
                    warnings.warn(
                        message=msg, category=DeprecationWarning, stacklevel=4
                    )
                case _:
                    pass
