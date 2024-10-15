#!/usr/bin/env python3
"""module that defines async_comprehension function"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """coroutine that collects 10 random numbers"""
    return [num async for num in async_generator()]
