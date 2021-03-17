#!/usr/bin/env python3
"""measure_runtime"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """[Coroutine that will execute async_comprehension four
        times in parallel using asyncio.gather and it shoul
        measure the total runtime]
    Args: no args
    Returns:
        float: [total time of execution]
    """
    start = time.perf_counter()
    res = await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter()
    total = (end - start)
    return total
