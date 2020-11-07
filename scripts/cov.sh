#!/bin/sh
pipenv run coverage run --branch -m pytest && pipenv run coverage html
