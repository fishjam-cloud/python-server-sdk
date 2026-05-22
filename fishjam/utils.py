from urllib.parse import urlparse

from fishjam.errors import MissingFishjamIdError, MissingManagementTokenError


def validate_fishjam_config(fishjam_id: str, management_token: str) -> None:
    if not fishjam_id:
        raise MissingFishjamIdError()
    if not management_token:
        raise MissingManagementTokenError()


def validate_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except AttributeError:
        return False


def get_fishjam_url(fishjam_id: str) -> str:
    if not validate_url(fishjam_id):
        return f"https://fishjam.io/api/v1/connect/{fishjam_id}"

    return fishjam_id
