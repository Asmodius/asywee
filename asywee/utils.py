import asyncio
import contextlib
import functools
import inspect

__all__ = [
    'patch',
    'future_iterator',
    'force_future',
    'ensure_iterables',
    'map_async',
]


@contextlib.contextmanager
def patch(obj, attr, value, default=None):
    original = getattr(obj, attr, default)
    setattr(obj, attr, value)
    yield
    setattr(obj, attr, original)


async def _future_item(future, index):
    return (await future)[index]


def future_iterator(future):
    index = 0
    while True:
        yield _future_item(future, index)
        index += 1


def ensure_iterables(*iterables, loop=None):
    for iterable in iterables:
        if inspect.isawaitable(iterable):
            future = asyncio.ensure_future(iterable, loop=loop)
            yield future_iterator(future)
        else:
            yield iterable


def force_future(entity, loop=None):
    if inspect.isawaitable(entity):
        return entity
    future = asyncio.Future(loop=loop)
    future.set_result(entity)
    return future


async def map_async(callback, *iterables, loop=None):
    futures = map(functools.partial(force_future, loop=loop), iterables)
    return map(callback, *await asyncio.gather(*futures, loop=loop))
