load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:py_library.bzl", "py_library")

py_library(
    name = "common",
    srcs = glob(["*.py"]),
    visibility = ["//visibility:public"],
    deps = [
        requirement("numpy"),  # Adds the external dependency
        requirement("pandas"),
        requirement("scipy"),
        requirement("scikit_learn"),
        requirement("matplotlib"),
    ],
)
