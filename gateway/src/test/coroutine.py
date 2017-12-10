#!/usr/bin/python3.5
#using coroutine of Python3.5
import asyncio
import time

now = lambda: time.time()
async def func(x):
    print('Waiting for %d s' % x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = now()

coro1 = func(1)
coro2 = func(2)
coro3 = func(4)

tasks = [
    asyncio.ensure_future(coro1),
    asyncio.ensure_future(coro2),
    asyncio.ensure_future(coro3)
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task return: ', task.result())

print('Program consumes: %f s' %  (now() - start))
