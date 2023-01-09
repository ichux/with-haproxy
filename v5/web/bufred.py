import logging.config
from itertools import cycle
from multiprocessing.managers import BaseManager
from xmlrpc.client import ServerProxy

SERVER_POOL = [
    f"{_.get('group')}:{_.get('name')}"
    for _ in ServerProxy(
        "http://admin:d5a122d9@localhost:9001/RPC2"
    ).supervisor.signalAllProcesses("data_science")
]
ITERATE_SERVER_URLS = cycle(SERVER_POOL)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)s]: %(message)s",
            "datefmt": "%d-%b-%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "console": {
            "handlers": ["console"],
            "level": "DEBUG",
            "formatter": "verbose",
        },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("console")


class RemoteManager(BaseManager):
    pass


RemoteManager.register("DynamicAIReport")
manager = RemoteManager(
    address=("0.0.0.0", int(next(ITERATE_SERVER_URLS).split(":")[1])),
    authkey=b"5a946d6066c1487",
)

try:
    manager.connect()

    air = getattr(manager, "DynamicAIReport")()
except ConnectionRefusedError as exc:
    logger.error("Network isn't reachable yet", exc_info=exc)


def bufio():
    with open("air_bufio.png", "wb") as img:
        img.write(air.bufio("img-1", 1, 2))

    with open("ong.png", "wb") as img:
        img.write(air.save_to())


if __name__ == "__main__":
    bufio()
