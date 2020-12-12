"""Invoke-based tasks."""
from invoke import task

stuff_to_analyze = "exact_cover_solver/ performance_tests/ tests/ tasks.py"


@task
def test(ctx):
    """Run unit tests."""
    ctx.run("pytest --cov=exact_cover_solver tests")


@task
def format(ctx):
    """Format project with black code formatter."""
    ctx.run(f"black {stuff_to_analyze}")


@task
def lint(ctx):
    """Lint project with flake8, black and mypy."""
    ctx.run(
        f"flake8 {stuff_to_analyze}; black --check {stuff_to_analyze}; "
        "mypy exact_cover_solver/"
    )


@task
def cov(ctx):
    """Generate coverage report based on test results."""
    ctx.run("python3 -m pytest --cov=exact_cover_solver tests --cov-report html")


@task
def docs(ctx):
    """Generate docs with pdoc and move them to correct folder."""
    ctx.run("pdoc --html --force --output-dir docs exact_cover_solver && ")
    ctx.run("cp -vaR docs/exact_cover_solver/. docs/ && rm -r docs/exact_cover_solver")
