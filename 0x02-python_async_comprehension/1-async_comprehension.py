#!/usr/bin/env python3
"""
module for async comperhention
"""
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    Import async_generator from the previous task
    then write a coroutine called async_comprehension that takes no arguments.

    The coroutine will collect 10 random numbers
    using an async comprehensing over async_generator,
    then return the 10 random numbers.
    """
    return [i async for i in async_generator()]
