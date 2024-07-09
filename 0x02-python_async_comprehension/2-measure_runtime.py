#!/usr/bin/env python3
"""
A module to measure run time
"""
async_comprehension = __import__()


async def measure_runtime() -> float:
    """
    Import async_comprehension from the previous file
    and write a measure_runtime coroutine that will execute
    async_comprehension four times in parallel using asyncio.gather.

    measure_runtime should measure the total runtime and return it.

    Notice that the total runtime is roughly 10 seconds,
    explain it to yourself.
    """
    start_time = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    end_time = time.perf_counter()
    return (end_time - start_time)
