#!/usr/python/env python3
""" define async_generator """
import asyncio
import random
from typing import List


async def async_generator() -> float:
    """
        loop 10 times, each time async wait 1sec
        & yield random numberi btw 0 & 10
    """
    for _ in range(10):
        # yield random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
