import sys
import logging
import mglearn.plot_helpers
from common import preamble
from mglearn import datasets


logger = logging.getLogger(__name__)


def configure_logger():
    handler = logging.StreamHandler(sys.stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)


configure_logger()


class Knearest():
    def __init__(self):
        self.X = None
        self.y = None

    def run(self):
        logger.info({"message": "Running Knearest"})
        self._generate_and_plot_dataset()

    def _generate_and_plot_dataset(self):
        self.X, self.y = datasets.make_forge()
        logger.debug({
            "message": "loaded data",
            "X": self.X,
            "y": self.y
        })
        # mglearn.plot_helpers.discrete_scatter(X[:, 0], X[:, 1]])
