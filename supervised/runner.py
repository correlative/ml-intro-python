
from supervised.twoclass import TwoClass
import supervised.skprtc as skprtc
from supervised.knnneighbor import (
    plot_knn_classification_euclidean,
    # plot_knn_classification_manhattan,
    plot_knn_classification_pairwise,
    # plot_knn_classification_cosine,
)


def run_two():
    TwoClass().fit()


if __name__ == "__main__":
    print(f" ############   START: supervise  ############# ")
    print("")
    run_two()
    print(" ----------------------------------------------- ")
    skprtc.print_iris()
    print(" ----------------------------------------------- ")
    print("")

    print(" ----------------------------------------------- ")
    print("")
    plot_knn_classification_euclidean(n_neighbors=3)
    # plot_knn_classification_manhattan(n_neighbors=3)
    plot_knn_classification_pairwise(n_neighbors=3)
    # plot_knn_classification_cosine(n_neighbors=3)
    print("")
    print(" ----------------------------------------------- ")
    print("")
    print(f" ############    END: supervise   ############# ")
