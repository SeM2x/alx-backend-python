#!/usr/bin/env python3
"""module that defines wait_random function"""
import asyncio
from random import random


async def wait_random(max_delay=10):
    """Wait for a random delay between 0 and `max_delay` seconds."""
    delay = random() * max_delay
    await asyncio.sleep(delay)
    return delay
