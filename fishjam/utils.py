from urllib.parse import urlparse

from fishjam.errors import MissingFishjamIdError

COMPOSITION_HOST = "https://rtc.fishjam.io"
LIVESTREAM_WHIP_PATH = "/api/v1/live/api/whip"
LIVESTREAM_WHEP_PATH = "/api/v1/live/api/whep"


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


def _livestream_url(fishjam_id: str, path: str) -> str:
    url = urlparse(get_fishjam_url(fishjam_id))

    return f"{url.scheme}://{url.netloc}{path}"


def get_livestream_whip_url(fishjam_id: str) -> str:
    """Resolve where a livestream is published, on the same host as Fishjam itself.

    Args:
        fishjam_id: The unique identifier for the Fishjam instance.

    Returns:
        The address a WHIP publisher sends the livestream to.
    """
    return _livestream_url(fishjam_id, LIVESTREAM_WHIP_PATH)


def get_livestream_whep_url(fishjam_id: str) -> str:
    """Resolve where a livestream is watched, on the same host as Fishjam itself.

    Args:
        fishjam_id: The unique identifier for the Fishjam instance.

    Returns:
        The address a WHEP viewer plays the livestream from.
    """
    return _livestream_url(fishjam_id, LIVESTREAM_WHEP_PATH)
