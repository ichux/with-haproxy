import concurrent.futures
import time


def square(n):
    # Simulate a long-running task by sleeping for 1 second
    time.sleep(1)
    return n**2


def main():
    # Create a ThreadPoolExecutor with 4 threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Submit 10 tasks to the executor
        results = [executor.submit(square, i) for i in range(10)]

        # Wait for the results to complete
        for future in concurrent.futures.as_completed(results):
            print(future.result())


if __name__ == "__main__":
    main()
