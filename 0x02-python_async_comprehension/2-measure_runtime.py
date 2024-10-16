#!/usr/bin/env python3

"""
Write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime should measure the total runtime and return it
    """
    start = time.time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
        )
    end = time.time()
    total_time = end - start
    return total_time
