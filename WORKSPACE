load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "4f7e2aa1eb9aa722d96498f5ef514f426c1f55161c3c9ae628c857a7128ceb07",
    strip_prefix = "rules_python-1.0.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/1.0.0/rules_python-1.0.0.tar.gz",
)


load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()


load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python_3_13",
    # Available versions are listed in @rules_python//python:versions.bzl.
    # We recommend using the same version your team is already standardized on.
    python_version = "3.13",
)

load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip_deps",
    python_interpreter_target = "@python_3_13_host//:python",
    requirements_lock = "//:requirements_lock.txt",
)

load("@pip_deps//:requirements.bzl", "install_deps")
install_deps()