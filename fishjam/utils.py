from asyncio import FIRST_COMPLETED, Event, ensure_future, wait
from typing import (
    AsyncIterator,
    Awaitable,
    Callable,
    TypeVar,
    cast,
)

from fishjam.errors import MissingFishjamIdError


def get_fishjam_url(fishjam_id: str | None, fishjam_url: str | None) -> str:
    if not fishjam_url and not fishjam_id:
        raise MissingFishjamIdError

    if fishjam_url:
        return fishjam_url

    return f"https://fishjam.io/api/v1/connect/{fishjam_id}"


_T = TypeVar("_T")


async def repeat_until(
    coro_fun: Callable[[], Awaitable[_T]],
    end_event: Event,
) -> AsyncIterator[_T]:
    while not end_event.is_set():
        end_fut = ensure_future(end_event.wait())
        done, _ = await wait(
            (ensure_future(coro_fun()), end_fut), return_when=FIRST_COMPLETED
        )
        for task in done:
            if task is end_fut:
                return
            yield cast(_T, await task)
