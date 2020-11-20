"""Invoke-based tasks."""
from invoke import task


@task
def start(ctx):
    """Start program with pypy implementation of python."""
    ctx.run("python3 exact_cover_solver/main.py")


@task
def test(ctx):
    """Run unit tests. Tests are run against cpython."""
    ctx.run("pytest --cov=exact_cover_solver tests")


@task
def format(ctx):
    """Format project with black code formatter."""
    ctx.run("black .")


@task
def lint(ctx):
    """Lint project with flake8 and black. This does not modify code, only checks."""
    ctx.run("flake8 . && black --check .")


@task
def cov(ctx):
    """Generate coverage report based on test results."""
    ctx.run("python3 -m pytest --cov=exact_cover_solver tests --cov-report html")


@task
def docs(ctx):
    """Generate docs with pdoc and move them to correct folder."""
    ctx.run("pdoc --html --force --output-dir docs exact_cover_solver")
    ctx.run("cp -vaR docs/exact_cover_solver/. docs/ && rm -r docs/exact_cover_solver")
