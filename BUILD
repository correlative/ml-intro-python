load("@rules_uv//uv:pip.bzl", "pip_compile")
load("@rules_uv//uv:venv.bzl", "create_venv")

pip_compile(
    name = "generate_requirements_txt",
    requirements_in = "//:requirements.txt", # default
    requirements_txt = "//:requirements_lock.txt", # default
)

create_venv(
    name = "create_venv",
    requirements_txt = "//:requirements_lock.txt", # default
)
