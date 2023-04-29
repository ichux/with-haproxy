import asyncio
import time
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


async def coro():
    # Define a coroutine that sleeps for 1 second
    await asyncio.sleep(1)


async def main():
    # Scenario 1: Run a single coroutine
    start_time = time.time()
    await coro()
    print("Scenario 1 elapsed time:", time.time() - start_time)

    # Scenario 2: Run 10 coroutines concurrently using asyncio.gather()
    coros = [coro() for _ in range(10)]
    start_time = time.time()
    await asyncio.gather(*coros)
    print("Scenario 2 elapsed time:", time.time() - start_time)

    # Scenario 3: Run 10 coroutines concurrently using asyncio.wait()
    coros = [coro() for _ in range(10)]
    start_time = time.time()
    done, pending = await asyncio.wait(coros, return_when=asyncio.ALL_COMPLETED)
    for task in done:
        await task
    print("Scenario 3 elapsed time:", time.time() - start_time)


if __name__ == "__main__":
    asyncio.run(main())
