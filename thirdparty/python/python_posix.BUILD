load("@rules_python//python:defs.bzl", "py_runtime")

package(default_visibility = ['//visibility:public'])

filegroup(
    name = "all_python_files",
    srcs = glob(["**/*"]),
)

py_runtime(
    name = "tab_python_runtime",
    # Exclude files with spaces in the name, because Bazel can't handle them.
    # https://github.com/bazelbuild/bazel/issues/4327
    files = glob(["**/*"], exclude=["**/* *"]),
    interpreter = "python",
    python_version = "PY3",
)
