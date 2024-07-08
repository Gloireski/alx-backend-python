#!/usr/bin/env python3
# 0-basic_async_syntax.py
import random
import asyncio


async def wait_random(max_delay=10):
    """ asynchronous coroutine """
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
