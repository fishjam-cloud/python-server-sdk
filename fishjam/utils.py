from urllib.parse import urlparse

from fishjam.errors import MissingFishjamIdError

COMPOSITION_HOST = "https://rtc.fishjam.io"


def validate_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except AttributeError:
        return False


def get_fishjam_url(fishjam_id: str) -> str:
    if not fishjam_id:
        raise MissingFishjamIdError()

    if not validate_url(fishjam_id):
        return f"https://fishjam.io/api/v1/connect/{fishjam_id}"

    return fishjam_id


def get_composition_url(composition_url: str | None = None) -> str:
    """Resolve the address of the Composition API, keeping only its origin.

    Args:
        composition_url: Address of the Composition API. Only needs setting when
            running against a deployment other than production.

    Returns:
        The origin the Composition API is reached at.
    """
    url = urlparse(composition_url or COMPOSITION_HOST)

    return f"{url.scheme}://{url.netloc}"
