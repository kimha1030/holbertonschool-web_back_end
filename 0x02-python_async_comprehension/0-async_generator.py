#!/usr/bin/env python3
"""async_generator"""

import random
import typing
import asyncio


async def async_generator() -> typing.Generator[float, None, None]:
    """[The coroutine will loop 10 times, each time asynchronously wait 1
        second, then yield a random number between 0 and 10. ]
    Args: no args
    Returns:
        float: [List of 10 random numbers between 0 and 10]
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
