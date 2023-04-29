import argparse
import io
import logging
import sys
from multiprocessing.managers import BaseManager

DESCRIPTION = """\
Share a global variable
--------------------------------
Share a variable to processes using
from multiprocessing.managers import BaseManager"""


class DynamicAIReport(object):
    @staticmethod
    def bufio(title, *args):
        pyplot.figure()
        pyplot.plot(args)
        pyplot.title(title)

        with io.BytesIO() as buffer:
            pyplot.savefig(buffer, format="png")
            buffer.seek(0)
            return buffer.read()

    @staticmethod
    def save_to(fc="g", title="Sample Visualization"):
        ys = 200 + numpy.random.randn(100)
        x = [x for x in range(len(ys))]
        pyplot.plot(x, ys, "-")
        pyplot.fill_between(x, ys, 195, where=(ys > 195), facecolor=fc, alpha=0.6)
        pyplot.title(title)

        with io.BytesIO() as buffer:
            pyplot.savefig(buffer, format="png")
            buffer.seek(0)
            return buffer.read()


class RemoteManager(BaseManager):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter, description=DESCRIPTION
    )

    parser.add_argument("-p", "--port", type=int, help="port to run on")
    pa = parser.parse_args()

    if not pa.port:
        parser.print_help()
        parser.exit(1)

    # import multiprocessing
    # mlt = multiprocessing.Manager()
    # port = mlt.Value("a", args.port)
    # state = mlt.Value("b", 0)
    # logging.info("port.value: %d", port.value)

    RemoteManager.register("DynamicAIReport", DynamicAIReport)

    RemoteManager(
        address=("0.0.0.0", pa.port),
        authkey=b"5a946d6066c1487",
    ).get_server().serve_forever()
