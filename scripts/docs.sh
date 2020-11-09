#!/bin/sh
# Generate docs
pipenv run pdoc --force --output-dir docs exact_cover_solver
# Move docs from exact_cover_solver package folder to docs
cp -vaR docs/exact_cover_solver/. docs/ && rm -r docs/exact_cover_solver
