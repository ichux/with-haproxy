import logging.config
import sys
from concurrent.futures import ThreadPoolExecutor as Executor
from multiprocessing.managers import BaseManager

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


RemoteManager.register("RemoteOperations")
manager = RemoteManager(
    address=("hxy-haproxy-if-web2-1", 5555), authkey=b"5a946d6066c1487a5f48a04d2b0af"
)

manager.connect()

remote_ops = getattr(manager, "RemoteOperations")()


def worker(times):
    logger.debug("iteration: %s", times)
    for _ in range(times):
        logger.info(remote_ops.model_data())


if __name__ == "__main__":
    with Executor(max_workers=10) as executor:
        future = executor.submit(worker, int(sys.argv[1]))
