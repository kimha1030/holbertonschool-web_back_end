#!/usr/bin/env python3
"""2-measure_runtime"""

import asyncio
import random
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """[Asynchronous coroutine that measures the total
        execution time for wait_n]

    Args:
        n (int): [number of iterations used with wait_random].
        max_delay (int): [maximun value of delay].

    Returns:
        float: [total time of execution]
    """

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total = (end - start) / n
    return total
