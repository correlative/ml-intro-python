load("@rules_jupyter//jupyter:jupyter_toolchain.bzl", "jupyter_toolchain")
load("@rules_uv//uv:pip.bzl", "pip_compile")
load("@rules_uv//uv:venv.bzl", "create_venv")

pip_compile(
    name = "generate_requirements_txt",
    requirements_in = "//:requirements.txt",  # default
    requirements_txt = "//:requirements_lock.txt",  # default
)

create_venv(
    name = "create_venv",
    requirements_txt = "//:requirements_lock.txt",  # default
)

jupyter_toolchain(
    ## the executable, defined in the rules_jupyter, allows configuration in a modular way
    name = "jup_toolchain",
    jupyter = "@pypi//jupyter",
    jupytext = "@pypi//jupytext",
    # Produced by rules_jupyter module extension.
    pandoc = "@pandoc",
    # Produced by rules_jupyter module extension.
    playwright_browsers_dir = "@rules_jupyter//playwright:current_browsers_dir",
)

toolchain(
    ## actual Bazel type of toolchain
    name = "jupyter_toolchain",
    toolchain = ":jup_toolchain",
    toolchain_type = "@rules_jupyter//jupyter:toolchain_type",
)
