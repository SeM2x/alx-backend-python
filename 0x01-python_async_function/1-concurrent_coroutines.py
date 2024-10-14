#!/usr/bin/env python3
'''module that defines wait_random function
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    '''Wait for a random delay between 0 and `max_delay` seconds
    '''
    delays = [await wait_random(max_delay) for i in range(n)]
    return sorted(delays)
