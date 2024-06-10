#!/usr/bin/env python3

'''
Import wait_random from the previous python file that you’ve written and write
an async routine called wait_n that takes in 2 int arguments
'''

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''return the list of all the delays (float values)
    '''
    waits = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(waits)
