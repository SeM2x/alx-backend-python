#!/usr/bin/env python3
"""module that defines wait_random function"""
import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and `max_delay` seconds."""
    delay: float = random() * max_delay
    await asyncio.sleep(delay)
    return delay

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))