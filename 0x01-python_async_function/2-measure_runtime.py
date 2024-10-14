#!/usr/bin/env python3
'''module that defines measure_time function
'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    ''' return the average time for `n` calls to `wait_n(n, max_delay)
    '''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
