import sys
import logging
import mglearn
import mglearn.plot_helpers
import mglearn.plots
from common import preamble
from mglearn import datasets
import numpy as np
import matplotlib.pyplot as plt

from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)


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

        self.X, self.y = datasets.load_extended_boston()
        print({"data_shape": (self.X.shape, self.y.shape)})

        mglearn.plots.plot_knn_classification(n_neighbors=3)
        plt.plot()
        plt.show()

        logger.info({"message": "Finished running Knearest"})




