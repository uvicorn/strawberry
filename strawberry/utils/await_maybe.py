import inspect
from typing import Awaitable, TypeVar, Union


T = TypeVar("T")

AwaitableOrValue = Union[Awaitable[T], T]


async def await_maybe(value: AwaitableOrValue):
    return await value if inspect.isawaitable(value) else value
