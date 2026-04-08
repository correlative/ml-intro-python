load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary")
load("@rules_python//python:py_library.bzl", "py_library")

py_library(
    name = "supervised_lib",
    srcs = glob(["*.py"]),
    data = glob(["data/*"]),
    deps = [
        requirement("numpy"),  # Adds the external dependency
        requirement("pandas"),
        requirement("scipy"),
        requirement("scikit_learn"),
        requirement("matplotlib"),
        "//common",
    ],
)

py_binary(
    name = "supervised_run",
    srcs = glob(["*.py"]),
    main = "runner.py",  # Explicitly sets the entry point
    deps = [
        ":supervised_lib",
        "//common",
        "@rules_python//python/runfiles",
    ],
)
