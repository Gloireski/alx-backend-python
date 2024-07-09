#!/usr/python/env python3
""" define async_generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        loop 10 times, each time async wait 1sec
        & yield random numberi btw 0 & 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
