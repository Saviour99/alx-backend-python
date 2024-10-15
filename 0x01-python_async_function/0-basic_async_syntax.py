#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an integer argument named wait_random
that waits for a random delay between 0 and max_delay
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    A function that returns an float
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay