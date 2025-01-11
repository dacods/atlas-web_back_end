#!/usr/bin/env python3
"""
async routine that takes in 2 int arguments
should return the list of all the delays
(float values). The list of the delays should be in ascending order without
using sort() because of concurrency.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    "return the list of all the delays"
    delays = []
    task = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*task)
    return sorted(delays)
