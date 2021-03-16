#!/usr/bin/env python3
"""4-tasks"""

import asyncio
import random
import typing

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """[Multiple asynchronous coroutines that return the list of all
        the delays]

    Args:
        n (int): [number of iterations used with wait_random].
        max_delay (int): [maximun value of delay].

    Returns:
        list: [list of all the delays as float values]
    """
    list_task = []
    for i in range(n):
        list_task.append(task_wait_random(max_delay))

    list_task_delay = []
    for task in asyncio.as_completed(list_task):
        task_delay: float = await task
        list_task_delay.append(task_delay)

    return list_task_delay
