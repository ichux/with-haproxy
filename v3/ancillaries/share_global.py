import datetime
import logging
import sys
from multiprocessing.managers import BaseManager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


class RemoteOperations:
    @staticmethod
    def bootstrap():
        return datetime.datetime.now().isoformat()

    model = bootstrap()

    def model_data(self):
        logging.info("fetching model_data")
        return self.model


class RemoteManager(BaseManager):
    pass


RemoteManager.register("RemoteOperations", RemoteOperations)
RemoteManager(
    address=("0.0.0.0", 12345), authkey=b"5a946d6066c1487a5f48a04d2b0af"
).get_server().serve_forever()
