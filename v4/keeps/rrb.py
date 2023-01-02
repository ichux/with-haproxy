import asyncio
from itertools import cycle

# dumb netcat server, short tcp connection
# $ ~  while true ; do nc -l 8888 < server1.html; done
# $ ~  while true ; do nc -l 9999 < server2.html; done
SERVER_POOL = [("haproxy-if-web1", 12345), ("haproxy-if-web2", 12345)]

# dumb python socket echo server, long tcp connection
# $ ~  while  python server.py
# SERVER_POOL = [('localhost', 6666)]

ITER = cycle(SERVER_POOL)

count = 0
period = 5


async def foo(n):
    global count
    global ITER

    while True:
        await asyncio.sleep(0)
        count += 1
        print("Foo", n, next(ITER))


async def main(delay):
    for n in range(1, 4):
        asyncio.create_task(foo(n))
    print("Testing for {:d} seconds".format(delay))
    await asyncio.sleep(delay)


asyncio.run(main(period))

print("Count =", count)
print("Coro executions per sec =", count / period)
