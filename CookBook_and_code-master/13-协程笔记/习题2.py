# 使用协程, 计算(a+b)*(c+d)

import asyncio
import time


async def calculate(a, b, c, d):
    x = a + b
    print(x, '=', a, '+', b, time.ctime())
    await asyncio.sleep(2)

    y = c + d
    print(y, '=', c, '+', d, time.ctime())
    await asyncio.sleep(2)

    z = x * y
    return z


async def plus(x, y):
    z = x + y
    print(z, '=', x, '+', y, time.ctime())
    await asyncio.sleep(2)
    return z


async def mul(x, y):
    z = x * y
    return z


loop = asyncio.get_event_loop()
task = asyncio.gather(plus(1, 3), plus(2, 4))

loop.run_until_complete(task)
x, y = task.result()
# loop.run_until_complete(asyncio.wait([mul(plus(1, 2), plus(3, 4))])
loop.close()


print(x * y, time.ctime())


