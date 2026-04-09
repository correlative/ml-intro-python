
import numpy as np
import pandas as pd
import os
from sklearn.datasets import load_iris


def print_iris():
    iris = load_iris()
    print(f"Data shape: {iris.data.shape}")
