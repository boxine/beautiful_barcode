install:
	pipenv install --dev

test:
	cd test && pipenv run python3 -m unittest

lint:
	pipenv run flake8 .

pypi:
	python3 setup.py sdist bdist_wheel upload

release: lint test
	if test -z "${VERSION}"; then echo VERSION missing; exit 1; fi
	sed -i "s#^\(__version__\s*=\s*'\)[^']*'\$$#\1${VERSION}'#" beautiful_barcode/__init__.py
	sed -i "s#^\(\s*version=\s*'\)[^']*\(',.*\)\$$#\1${VERSION}\2#" setup.py
	git diff
	git add beautiful_barcode/__init__.py setup.py
	git commit -m "release ${VERSION}"
	git tag "v${VERSION}"
	git push
	git push --tags
	$(MAKE) pypi

.PHONY: install test lint pypi release
