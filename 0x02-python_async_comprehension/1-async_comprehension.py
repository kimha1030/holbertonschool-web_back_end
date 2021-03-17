#!/usr/bin/env python3
"""async_comprehension"""

import random
import typing
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """[The coroutine will collect 10 random numbers using an
        async comprehensing over async_generator]
    Args: no args
    Returns:
        float: [list of 10 random numbers between 0 and 10]
    """
    result = [i async for i in async_generator()]
    return result
