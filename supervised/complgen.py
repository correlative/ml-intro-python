import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def compl_gen() -> None:
    cancer = load_breast_cancer()
    # https://stackoverflow.com/questions/34842405/parameter-stratify-from-method-train-test-split-scikit-learn/38889389#38889389
    X_train, X_test, y_train, y_test = train_test_split(
        cancer.data,
        cancer.target,
        stratify=cancer.target,
        random_state=66
    )

    training_accuracy = []
    test_accuracy = []

    neighbor_settings = range(1, 11)

    for setting in neighbor_settings:
        clf = KNeighborsClassifier(n_neighbors=setting)
        clf.fit(X_train, y_train)

        # record training set accuracy
        training_accuracy.append(clf.score(X_train, y_train))
        test_accuracy.append(clf.score(X_test, y_test))

    print(neighbor_settings)
    print(training_accuracy)
    print(test_accuracy)

    plt.plot(neighbor_settings, training_accuracy, label="Training Accuracy")
    plt.plot(neighbor_settings, test_accuracy, label="Test Accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("Neighbors")
    plt.legend(loc="lower right")
    plt.show()
