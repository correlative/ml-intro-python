import numpy as np
import pandas as pd
import os
from scipy import signal
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.datasets import make_blobs
from sklearn.utils import Bunch
import matplotlib.pyplot as plt

from common.datautil import make_forge
from common.plot_helpers import discrete_scatter


class TwoClass:
    def __init__(self):
        self.name = 'TwoClass'

    def fit(self) -> None:
        X, y = make_forge()
        discrete_scatter(X[:, 0], X[:, 1], y)
        plt.legend(["Class 0", "Class 1"], loc=4)
        plt.xlabel("First feature")
        plt.ylabel("Second feature")
        # plt.show()

        print("X.shape :::::", X.shape)
