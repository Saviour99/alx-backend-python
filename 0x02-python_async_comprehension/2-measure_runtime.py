#!/usr/bin/env python3

"""
Write a coroutine called measure_runtime that will execute async_comprehension
four times in parallel using asyncio.gather.
"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This coroutine will execute async_comprehension four times in parallel
    and measure the total runtime

    Returns:
        The total runtime of running async_comprehension four times
        in parallel.
    """
    start_time = time.perf_counter()  # Start timer

    # Run async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()  # End timer

    # Return the total runtime
    return end_time - start_time
