'''
It is a module for asynchronous programming.
Used for I/O bound tasks.
Runs many tasks concurrently in one thread/.
'''

import asyncio

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished after {delay} seconds")

async def main():
    await asyncio.gather(task("A", 1),
                         task("B", 3),
                         task("C", 2))

asyncio.run(main())
