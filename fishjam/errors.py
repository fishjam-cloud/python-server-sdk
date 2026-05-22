from http import HTTPStatus

from fishjam._openapi_client.models import Error
from fishjam._openapi_client.types import Response


class MissingFishjamIdError(ValueError):
    def __init__(self) -> None:
        super().__init__("Fishjam ID is required")


class MissingManagementTokenError(ValueError):
    def __init__(self) -> None:
        super().__init__("Management Token is required")


class HTTPError(Exception):
    """"""

    @staticmethod
    def from_response(response: Response[Error]):
        """@private"""
        if not response.parsed:
            raise RuntimeError("Got endpoint error reponse without parsed field")

        errors = response.parsed.errors

        match response.status_code:
            case HTTPStatus.BAD_REQUEST:
                return BadRequestError(errors)

            case HTTPStatus.UNAUTHORIZED:
                return UnauthorizedError(errors)

            case HTTPStatus.NOT_FOUND:
                return NotFoundError(errors)

            case HTTPStatus.SERVICE_UNAVAILABLE:
                return ServiceUnavailableError(errors)

            case HTTPStatus.CONFLICT:
                return ConflictError(errors)

            case _:
                return InternalServerError(errors)


class BadRequestError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class UnauthorizedError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class NotFoundError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class ServiceUnavailableError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class InternalServerError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class ConflictError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)
