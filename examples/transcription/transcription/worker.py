from asyncio import Task, TaskGroup
from contextlib import asynccontextmanager
from typing import Any, Coroutine


class BackgroundWorker:
    def __init__(self, tg: TaskGroup) -> None:
        self._tg = tg
        self._tasks: set[Task[None]] = set()

    def run_in_background(self, coro: Coroutine[Any, Any, None]):
        task = self._tg.create_task(coro)
        task.add_done_callback(self._remove_task)
        self._tasks.add(task)
        return task

    def _remove_task(self, task: Task[None]):
        self._tasks.discard(task)

    def cleanup(self):
        for task in self._tasks:
            task.cancel()
        self._tasks = set()


@asynccontextmanager
async def async_worker():
    async with TaskGroup() as tg:
        worker = BackgroundWorker(tg)
        yield worker
        worker.cleanup()
