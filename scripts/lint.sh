#!/bin/sh
pipenv run flake8 . && pipenv run black --check .
