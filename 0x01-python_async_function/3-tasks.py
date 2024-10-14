#!/usr/bin/env python3
'''module that defines task_wait_random function
'''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' return a asyncio.Task
    '''
    return asyncio.create_task(wait_random(max_delay))
