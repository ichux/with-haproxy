import asyncio

num_coros = (100, 200, 500, 1000)
iterations = [0, 0, 0, 0]
duration = 2  # Time to run for each number of coros
count = 0
done = False


async def foo():
    global count
    while True:
        await asyncio.sleep(0)
        count += 1


async def test():
    global count, done
    old_n = 0
    for n, n_coros in enumerate(num_coros):
        print("Testing {} coros for {}secs".format(n_coros, duration))
        count = 0
        for _ in range(n_coros - old_n):
            asyncio.create_task(foo())
        old_n = n_coros
        await asyncio.sleep(duration)
        iterations[n] = count
    done = True


async def report():
    asyncio.create_task(test())
    while not done:
        await asyncio.sleep(1)
    for x, n in enumerate(num_coros):
        print(
            "Coros {:4d}  Iterations/sec {:5d}  Duration {:3d}us".format(
                n,
                int(iterations[x] / duration),
                int(duration * 1000000 / iterations[x]),
            )
        )


asyncio.run(report())
