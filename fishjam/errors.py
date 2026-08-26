from http import HTTPStatus

from fishjam._openapi_client.models import Error
from fishjam._openapi_client.types import Response


class MissingFishjamIdError(ValueError):
    def __init__(self) -> None:
        super().__init__("Fishjam ID is required")


class StaleSdkError(Exception):
    def __init__(self, status: int) -> None:
        super().__init__(
            f"Received a recording status this SDK cannot parse ({int(status)})."
            " You are probably using an outdated version of fishjam-server-sdk"
            " - please update it."
        )
        self.status = int(status)
        """Raw wire value received from the server."""


class HTTPError(Exception):
    """"""

    @staticmethod
    def from_response(response: Response[Error]):
        """@private"""
        if response.parsed:
            errors = response.parsed.errors
        else:
            errors = response.content.decode(errors="replace")

        return error_for_status(response.status_code, errors)


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


class CompositionNotFoundError(NotFoundError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class InputNotFoundError(NotFoundError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class OutputNotFoundError(NotFoundError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class RendererNotFoundError(NotFoundError):
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


class QuotaExceededError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class InvalidFishjamCredentialsError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


def error_for_status(
    status_code: HTTPStatus, messages, not_found: type["HTTPError"] | None = None
) -> HTTPError:
    """@private"""
    match status_code:
        case HTTPStatus.BAD_REQUEST | HTTPStatus.UNPROCESSABLE_ENTITY:
            return BadRequestError(messages)

        case HTTPStatus.UNAUTHORIZED:
            return UnauthorizedError(messages)

        case HTTPStatus.PAYMENT_REQUIRED:
            return QuotaExceededError(messages)

        case HTTPStatus.NOT_FOUND:
            return (not_found or NotFoundError)(messages)

        case HTTPStatus.CONFLICT:
            return ConflictError(messages)

        case HTTPStatus.SERVICE_UNAVAILABLE:
            return ServiceUnavailableError(messages)

        case _:
            return InternalServerError(messages)
