import argparse
import logging
import sys
from itertools import cycle
import time
from multiprocessing.managers import BaseManager

count = 0

DESCRIPTION = """\
Share a global variable
--------------------------------
Share a variable to processes using
from multiprocessing.managers import BaseManager"""

SERVER_POOL = [("haproxy-if-web1", 12345), ("haproxy-if-web2", 12345)]
ITERATE = cycle(SERVER_POOL)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


class NextServer:
    @staticmethod
    def server():
        global count

        count += 1
        logging.info(f"+: PORT ({args.port}) | count: {count} | {time.perf_counter_ns()}")
        return next(ITERATE)


class RemoteManager(BaseManager):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter, description=DESCRIPTION
    )

    parser.add_argument("-p", "--port", type=int, help="port to run on")
    args = parser.parse_args()

    if not args.port:
        parser.print_help()
        parser.exit(1)

    # import multiprocessing
    # mlt = multiprocessing.Manager()
    # port = mlt.Value("a", args.port)
    # state = mlt.Value("b", 0)
    # logging.info("port.value: %d", port.value)

    RemoteManager.register("NextServer", NextServer)
    RemoteManager(
        address=("0.0.0.0", args.port), authkey=b"5a946d6066c1487"
    ).get_server().serve_forever()
