import asyncio
import time


async def square(n):
    # Simulate a long-running task by sleeping for 1 second
    await asyncio.sleep(1)
    return n**2


async def main():
    # Create an event loop
    loop = asyncio.get_running_loop()

    # Schedule 10 coroutines to run concurrently
    coros = [square(i) for i in range(10)]
    results = await asyncio.gather(*coros)

    # Print the results
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
