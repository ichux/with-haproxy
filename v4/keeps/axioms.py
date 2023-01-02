import asyncio
import time
from itertools import cycle

SERVER_POOL = [("haproxy-if-web1", 12345), ("haproxy-if-web2", 12345)]
ITER = cycle(SERVER_POOL)


# import aiohttp
# from random import randint
# proxy_list = [
#   'http://Username:Password@85.237.57.198:20000',
#   'http://Username:Password@85.237.57.198:21000',
#   'http://Username:Password@85.237.57.198:22000',
#   'http://Username:Password@85.237.57.198:23000',
#               ]
#
# proxy_index = randint(0, len(proxy_list) - 1)
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#             async with session.get('http://httpbin.org/get', proxy=proxy_list[proxy_index]) as resp:
#                 print(resp.status)
#                 print(await resp.text())
#
# asyncio.run(main)


def blocking_io(tick):
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(tick)
    print(f"sA at {next(ITER)}")
    print(f"blocking_io complete at {time.strftime('%X')}")


async def main():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(asyncio.to_thread(blocking_io, 1), asyncio.sleep(1))

    print(f"finished main at {time.strftime('%X')}")


asyncio.run(main())
