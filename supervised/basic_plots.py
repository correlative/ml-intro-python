import sys
import logging
import mglearn.plot_helpers
from common import preamble
from mglearn import datasets
import numpy as np
from sklearn.datasets import load_breast_cancer

import matplotlib.pyplot as plt


logger = logging.getLogger(__name__)


def configure_logger():
    handler = logging.StreamHandler(sys.stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)


configure_logger()


class BasicPlots():
    def run(self):
        self._data_details()
        self._generate_and_plot_dataset()

    def _data_details(self):
        self.cancer = load_breast_cancer()
        logger.info({"data_keys": self.cancer.keys(), "shape": self.cancer.data.shape})
        logger.warning({"count_per_class": {n: v for n, v in zip(self.cancer.target_names, np.bincount(self.cancer.target))}})

    def _generate_and_plot_dataset(self):
        self.X, self.y = datasets.make_forge()
        logger.info({
            "message": "loaded data",
            "X": self.X.shape,
            "y": self.y.shape
        })

        logger.info({
            "message": "loaded data details",
            "X": self.X,
            "y": self.y
        })
        mglearn.plot_helpers.discrete_scatter(self.X[:, 0], self.X[:, 1], self.y)
        plt.legend(["Class 0", "Class 1"], loc=4)
        plt.xlabel("First feature")
        plt.ylabel("Second feature")
        plt.plot(self.X, self.y, 0)
        plt.show()
