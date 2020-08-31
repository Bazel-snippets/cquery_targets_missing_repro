workspace(name = "cquery_targets_missing_repro")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.0.2/rules_python-0.0.2.tar.gz",
    strip_prefix = "rules_python-0.0.2", 
    sha256 = "b5668cde8bb6e3515057ef465a35ad712214962f0b3a314e551204266c7be90c",
)
load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

http_archive(
    name = "python_windows",
    build_file = "//thirdparty/python:python_windows.BUILD",
    sha256 = "de59a3544c17dd091c08a6a061fb2660d3bdbd667ed6617b01189a86c18ac2c0",
    url = "https://www.python.org/ftp/python/3.8.5/python-3.8.5-embed-amd64.zip", 
)

new_local_repository(
    name = "python_linux",
    path = "./pseudo_python/",
    build_file = "//thirdparty/python:python_posix.BUILD",
)

new_local_repository(
    name = "python_osx",
    path = "./pseudo_python/",
    build_file = "//thirdparty/python:python_posix.BUILD",
)

register_toolchains(":tab_python_toolchain")