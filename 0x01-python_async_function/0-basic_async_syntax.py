#!/usr/bin/env python3
"""0-basic_async_syntax"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """[Asynchronous coroutine that waits for a random
        delay between 0 and max_delay]

    Args:
        max_delay (int): [maximun value of delay]. Defaults to 10.

    Returns:
        float: [random number between 0 and max_delay]
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
