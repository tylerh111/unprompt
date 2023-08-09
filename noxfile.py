import argparse
import glob
import os
import pathlib
from typing import Any, List, Mapping, Sequence

import nox
import setuptools_scm

nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["lint"]

DIST = "dist"
VERSION = setuptools_scm.get_version(version_scheme="no-guess-dev")

REQUIREMENTS = {
    "docs": "requirements/docs.txt",
    "tests": "requirements/tests.txt",
}


def _add_args_if(
    test: bool,
    *args: str,
):
    """Usage: `*_add_args_if(...)`"""
    return args if test else ()


def _parse_args(
    args: Sequence[str],
    name: str,
    *options: Mapping[str, Any],
    description: str = None,
    epilog: str = None,
    command: str = None,
    add_ellipse_to_usage: bool = True,
):
    """Usage: _parser_args(session.posargs, <name>, <argument>, ...)"""

    class EllipsisHelpFormatter(argparse.RawTextHelpFormatter):
        @staticmethod
        def _add_ellipse_to_usage(usage: str):
            if not add_ellipse_to_usage:
                return usage
            has_newline = usage.endswith("\n")
            usage = usage.rstrip("\n")
            usage = (usage + " ...") if not usage.endswith("...") else usage
            usage = (usage + "\n") if has_newline else usage
            return usage

        def format_help(self):
            help = super().format_help()
            if help:
                usage, *help = help.splitlines(keepends=True)
                usage = self._add_ellipse_to_usage(usage)
                help = "".join((usage, *help))
            return help

    if not command:
        command = "underlying command(s)"

    if not epilog:
        epilog = f"remaining:\n  passed to {command}"

    parser = argparse.ArgumentParser(
        prog=name,
        description=description,
        formatter_class=EllipsisHelpFormatter,
        epilog=epilog,
    )
    for option in options:
        names = option.pop("args")
        names = [names] if isinstance(names, str) else names
        parser.add_argument(*names, **option)

    return parser.parse_known_intermixed_args(args)


# =============================================================================
#  development commands
# =============================================================================


@nox.session
@nox.parametrize(
    "formatter",
    ["black", "isort"],
    ["black", "isort"],
)
def format(session: nox.Session, formatter: str):
    """Run formatters"""
    args, remaining = _parse_args(
        session.posargs,
        "nox -s format",
        dict(
            args="--fix",
            action="store_true",
            default=False,
            help="write format changes",
        ),
        dict(
            args="--no-fix",
            action="store_false",
            dest="fix",
            help="no write format changes",
        ),
        command=formatter,
    )

    fix: bool = args.fix

    # fmt: off
    def black_cmd():
        return [
            "black",
            ".",
            *_add_args_if(not fix, "--check"),
        ]

    def isort_cmd():
        return [
            "isort",
            ".",
            *_add_args_if(not fix, "--check"),
            *_add_args_if(not fix, "--diff"),
        ]
    # fmt: on

    if formatter == "black":
        session.install("black")
        session.run(*black_cmd(), *remaining)
    if formatter == "isort":
        session.install("isort")
        session.run(*isort_cmd(), *remaining)


@nox.session
def test(session: nox.Session):
    """Run tests"""
    session.install("-e", ".")
    session.install("-r", REQUIREMENTS["tests"])
    session.run(
        "pytest",
        "tests",
        *session.posargs,
    )


@nox.session
def coverage(session: nox.Session):
    """Run coverage"""
    session.install("-e", ".")
    session.install("-r", REQUIREMENTS["tests"])
    session.run(
        "pytest",
        "--cov=unprompt",
        "--cov-report=xml:.coverage.xml",
        *session.posargs,
    )


@nox.session
@nox.parametrize(
    "linter",
    ["ruff", "mypy"],
    ["ruff", "mypy"],
)
def lint(session: nox.Session, linter: str):
    """Run linters"""

    # fmt: off
    def ruff_cmd():
        return [
            "ruff",
            "check",
            "--exit-zero",
            "--force-exclude",
            ".",
        ]

    def mypy_cmd():
        return [
            "mypy",
            "--pretty",
            "--show-error-codes",
            ".",
        ]
    # fmt: on

    if linter == "ruff":
        session.install("ruff")
        session.log("# Running ruff")
        session.run(*ruff_cmd(), *session.posargs)
    if linter == "mypy":
        session.install("mypy")
        session.log("# Running mypy")
        session.run(*mypy_cmd(), *session.posargs, success_codes=(0, 1))


@nox.session(name="docs")
def build_docs(session: nox.Session):
    """Build documentation"""
    docs = pathlib.Path("docs")

    # fmt: off
    def sphinx_build_command(kind: str) -> List[str]:
        return [
            "sphinx-build",
            "--keep-going",
            "-W",
            "-c", docs,
            "-d", docs / "_build" / "doctrees",
            "-b", kind,
            docs,
            docs / "_build" / kind,
        ]
    # fmt: on

    session.install("-e", ".")
    session.install("-r", REQUIREMENTS["docs"])
    session.log("# Building documentation")
    session.run(*sphinx_build_command("html"), *session.posargs)


# =============================================================================
#  release commands
# =============================================================================


@nox.session(name="prepare-release")
def prepare_release(session: nox.Session):
    """Prepare release"""
    version = VERSION
    args = session.posargs or ["-m", "--allow-dirty"]

    session.install("bumpver")
    session.log(f"# Currently version {version!r}")
    session.run("bumpver", "update", *args)


@nox.session(name="build")
def build_release(session: nox.Session):
    """Build release"""
    dist = pathlib.Path(DIST)

    if os.path.exists(dist) and os.listdir(dist):
        session.error(
            f"There are files in {dist!r}. Remove them and try again. "
            f"Use `git clean -fxdi -- {dist!r}` command to do this."
        )

    session.install("build", "twine")
    session.log("# Building distribution")
    session.run("python", "-m", "build", *session.posargs)

    distribution_files = glob.glob(f"{dist}/*")
    session.log(f'# Verifying distribution: {", ".join(distribution_files)}')
    session.run("twine", "check", *distribution_files)


@nox.session(name="deploy")
def upload_release(session: nox.Session):
    """Deploy release"""
    dist = pathlib.Path(DIST)
    version = VERSION

    distribution_files = glob.glob(f"{dist}/*")
    distribution_files = glob.glob(f"{dist}/*")
    session.log(f'# Distribution files: {", ".join(distribution_files)}')

    # make sure only 2 distribution files
    count = len(distribution_files)
    if count != 2:
        session.error(
            f"Expected 2 distribution files for upload, got {count} "
            f"Remove {dist!r} and run `nox -s build-release`"
        )

    # make sure files are correctly named
    distribution_filenames = [os.path.basename(f) for f in distribution_files]
    distribution_filenames_expected = [
        f"unprompt-{version}-py3-none-any.whl",
        f"unprompt-{version}.tar.gz",
    ]
    if sorted(distribution_filenames) != sorted(
        distribution_filenames_expected
    ):
        session.error(
            f"Distribution files do not seeem to be for {version} release."
        )

    session.install("twine")
    session.run(
        "twine",
        "upload",
        *distribution_files,
        *session.posargs,
    )
