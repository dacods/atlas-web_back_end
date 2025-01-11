#!/usr/bin/env python3
"""
Altering old function to new function
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    "return the list of all the delays"
    delays = []
    task = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*task)
    return sorted(delays)
