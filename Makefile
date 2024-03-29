SHELL := /bin/bash
MAX_LINE_LENGTH := 119
POETRY_VERSION := $(shell poetry --version 2>/dev/null)

help: ## List all commands
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9 -]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

check-poetry:
	@if [[ "${POETRY_VERSION}" == *"Poetry"* ]] ; \
	then \
		echo "Found ${POETRY_VERSION}, ok." ; \
	else \
		echo 'Please install poetry first, with e.g.:' ; \
		echo 'make install-poetry' ; \
		exit 1 ; \
	fi

install-poetry: ## install or update poetry
	@if [[ "${POETRY_VERSION}" == *"Poetry"* ]] ; \
	then \
		echo 'Update poetry v$(POETRY_VERSION)' ; \
		poetry self update ; \
	else \
		echo 'Install poetry' ; \
		curl -sSL "https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py" | python3 ; \
	fi

install: check-poetry ## install via poetry
	poetry install

update: check-poetry ## Update the dependencies as according to the pyproject.toml file
	poetry update

lint: ## Run code formatters and linter
	poetry run flynt --fail-on-change -ll ${MAX_LINE_LENGTH} beautiful_barcode
	poetry run isort --check-only beautiful_barcode
	poetry run flake8 beautiful_barcode

fix-code-style: ## Fix code formatting
	poetry run flynt -ll ${MAX_LINE_LENGTH} beautiful_barcode
	poetry run autopep8 --ignore-local-config --max-line-length=${MAX_LINE_LENGTH} --aggressive --aggressive --in-place --recursive beautiful_barcode
	poetry run isort beautiful_barcode

tox-listenvs: check-poetry ## List all tox test environments
	poetry run tox --listenvs

tox: check-poetry ## Run pytest via tox with all environments
	poetry run tox

tox-py36: check-poetry ## Run pytest via tox with *python v3.6*
	poetry run tox -e py36

tox-py37: check-poetry ## Run pytest via tox with *python v3.7*
	poetry run tox -e py37

tox-py38: check-poetry ## Run pytest via tox with *python v3.8*
	poetry run tox -e py38

tox-py39: check-poetry ## Run pytest via tox with *python v3.9*
	poetry run tox -e py39

pytest: check-poetry ## Run pytest
	poetry run pytest

pytest-ci: check-poetry ## Run pytest with CI settings
	poetry run pytest -c pytest-ci.ini

publish: ## Release new version to PyPi
	poetry run ./publish.py

examples: example_inkscape.svg example_path.svg example_simple.svg  ## Regenerate example files

example_inkscape.svg: | beautiful_barcode
	poetry run python -m beautiful_barcode -r inkscape -o example_inkscape.svg 123456789012

example_path.svg: | beautiful_barcode
	poetry run python -m beautiful_barcode -r path -o example_path.svg 123456789012

example_simple.svg: | beautiful_barcode
	poetry run python -m beautiful_barcode -r simple -o example_simple.svg 123456789012

.PHONY: help install lint fix pytest publish examples