import argparse
import logging
import multiprocessing
import sys
from itertools import cycle
from multiprocessing.managers import BaseManager

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
        state.value += 1

        logging.info(f"+: {port.value} | {state.value}")
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

    mlt = multiprocessing.Manager()
    port = mlt.Value("a", args.port)
    state = mlt.Value("b", 0)

    RemoteManager.register("NextServer", NextServer)
    RemoteManager(
        address=("0.0.0.0", port.value), authkey=b"5a946d6066c1487"
    ).get_server().serve_forever()
