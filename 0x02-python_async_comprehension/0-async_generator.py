#!/usr/bin/env python3
"""module that defines async_generator function"""
import asyncio
import random
import typing


async def async_generator() -> typing.AsyncGenerator[float]:
    """coroutine that yields random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
