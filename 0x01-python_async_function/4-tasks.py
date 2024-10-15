#!/usr/bin/env python3

"""
Let's execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List
import random


async def task_wait_random(max_delay: int = 10) -> float:
    """
    A function that returns an float
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that spawns wait_random n times with a max delay
    and returns the
    list of all delays in ascending order.
    """

    ts = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]

    delays = await asyncio.gather(*ts)

    sorted_delays = []
    while delays:
        smallest = min(delays)
        sorted_delays.append(smallest)
        delays.remove(smallest)

    return sorted_delays
