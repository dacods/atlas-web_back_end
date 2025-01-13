#!/usr/bin/env python3
"""
coroutine that will execute four times in parallel using asyncio.gather
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    "Returns total runtime"
    start = time.time()
    parallel = await asyncio.gather(async_comprehension(),
                                    async_comprehension(),
                                    async_comprehension(),
                                    async_comprehension()
                                    )
    end = time.time()
    total_time = end - start
    return total_time
