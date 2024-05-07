#!/usr/bin/env python3
"""2-measure_runtime.py"""

import asyncio
from time import perf_counter
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it."""
    start_time = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = perf_counter()
    return end_time - start_time
