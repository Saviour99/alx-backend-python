#!/usr/bin/env python3

"""
Let's execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that spawns wait_random n times with a max delay and returns the
    list of all delays in ascending order.
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays = await asyncio.gather(*tasks)

    sorted_delays = []
    while delays:
        smallest = min(delays)
        sorted_delays.append(smallest)
        delays.remove(smallest)

    return sorted_delays
