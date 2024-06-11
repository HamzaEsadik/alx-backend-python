#!/usr/bin/env python3
'''
collect 10 random numbers using an async comprehensing over async_generator,
then return the 10 random numbers.
'''

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''
    Creates a list of 10 numbers.
    '''
    return [rand async for rand in async_generator()]
