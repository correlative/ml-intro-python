import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import (
    euclidean_distances,
    pairwise_distances,
    # manhattan_distances,
    # cosine_similarity,
)
from sklearn.neighbors import KNeighborsClassifier

from common.datautil import make_forge
from common.plot_helpers import discrete_scatter


X_TEST = np.array([[8.2, 3.66214339], [9.9, 3.2], [11.2, .5]])


def plot_knn_classification_euclidean(n_neighbors=1):
    X, y = make_forge()

    dist = euclidean_distances(X, X_TEST)
    closest = np.argsort(dist, axis=0)

    for x, neighbors in zip(X_TEST, closest.T):
        for neighbor in neighbors[:n_neighbors]:
            plt.arrow(
                x[0],
                x[1],
                X[neighbor, 0] - x[0],
                X[neighbor, 1] - x[1],
                head_width=0, fc='k',
                ec='k'
            )

    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
    test_points = discrete_scatter(X_TEST[:, 0], X_TEST[:, 1], clf.predict(X_TEST), markers="*")
    training_points = discrete_scatter(X[:, 0], X[:, 1], y)
    plt.legend(
        training_points + test_points,
        [
            "EU : training class 0",
            "EU : training class 1",
            "EU : test pred 0",
            "EU : test pred 1"
        ]
    )
    plt.show()


# def plot_knn_classification_manhattan(n_neighbors=1):
#     X, y = make_forge()
#
#     dist = manhattan_distances(X, X_TEST)
#     closest = np.argsort(dist, axis=0)
#
#     for x, neighbors in zip(X_TEST, closest.T):
#         for neighbor in neighbors[:n_neighbors]:
#             plt.arrow(
#                 x[0],
#                 x[1],
#                 X[neighbor, 0] - x[0],
#                 X[neighbor, 1] - x[1],
#                 head_width=0, fc='k',
#                 ec='k'
#             )
#
#     clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
#     test_points = discrete_scatter(X_TEST[:, 0], X_TEST[:, 1], clf.predict(X_TEST), markers="*")
#     training_points = discrete_scatter(X[:, 0], X[:, 1], y)
#     plt.legend(
#         training_points + test_points,
#         [
#             "MN : training class 0",
#             "MN : training class 1",
#             "MN : test pred 0",
#             "MN : test pred 1"
#         ]
#     )
#     plt.show()


def plot_knn_classification_pairwise(n_neighbors=1):
    X, y = make_forge()

    dist = pairwise_distances(X, X_TEST)
    closest = np.argsort(dist, axis=0)

    for x, neighbors in zip(X_TEST, closest.T):
        for neighbor in neighbors[:n_neighbors]:
            plt.arrow(
                x[0],
                x[1],
                X[neighbor, 0] - x[0],
                X[neighbor, 1] - x[1],
                head_width=0, fc='k',
                ec='k'
            )

    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
    test_points = discrete_scatter(X_TEST[:, 0], X_TEST[:, 1], clf.predict(X_TEST), markers="*")
    training_points = discrete_scatter(X[:, 0], X[:, 1], y)
    plt.legend(
        training_points + test_points,
        [
            "PR : training class 0",
            "PR : training class 1",
            "PR : test pred 0",
            "PR : test pred 1"
        ]
    )
    plt.show()


# def plot_knn_classification_cosine(n_neighbors=1):
#     X, y = make_forge()
#
#     dist = cosine_similarity(X, X_TEST)
#     closest = np.argsort(dist, axis=0)
#
#     for x, neighbors in zip(X_TEST, closest.T):
#         for neighbor in neighbors[:n_neighbors]:
#             plt.arrow(
#                 x[0],
#                 x[1],
#                 X[neighbor, 0] - x[0],
#                 X[neighbor, 1] - x[1],
#                 head_width=0, fc='k',
#                 ec='k'
#             )
#
#     clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
#     test_points = discrete_scatter(X_TEST[:, 0], X_TEST[:, 1], clf.predict(X_TEST), markers="*")
#     training_points = discrete_scatter(X[:, 0], X[:, 1], y)
#     plt.legend(
#         training_points + test_points,
#         [
#             "CS : training class 0",
#             "CS : training class 1",
#             "CS : test pred 0",
#             "CS : test pred 1"
#         ]
#     )
#     plt.show()
