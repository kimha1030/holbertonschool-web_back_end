#!/usr/bin/env python3
"""3-tasks"""

import asyncio
import random
import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """[Function that return a asyncio task]

    Args:
        max_delay (int): [maximun value of delay].

    Returns:
        asyncio.Task
    """

    createTask = asyncio.create_task(wait_random(max_delay))
    return createTask
