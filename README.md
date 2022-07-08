# beautiful_barcode
Generate well-formatted, production-ready Barcodes.

By default, existing Python barcode libraries like [python-barcode](https://pypi.org/project/python-barcode/) generate good barcodes, but any and all formatting of the text is left up to the user. beautiful_barcode generates a nicely formatted barcode with interleaved text out of the box:

![Example barcode](example_path.svg)

Depending on your renderer (and true by default), text in the barcode is *not* an SVG `<text>` element, as such an elment may render differently on different machines depending on font availability.

This library is currently limited to UPC-A/EAN and EPS/SVG – that's all we (the original authors) needed. Patches welcome!

# Installation

```sh
$ pip install beautiful_barcode
```

# Usage

```
>>> from beautiful_barcode import gtin
>>> gtin('123456789012').write('output.svg')
```

Command line:

```sh
$ python -m beautiful_barcode 123456789012 -o output.svg
```

## Quickstart

```bash
~$ git clone https://github.com/boxine/beautiful_barcode.git
~$ cd beautiful_barcode
~/beautiful_barcode$ make
help                 List all commands
install-poetry       install or update poetry
install              install via poetry
update               Update the dependencies as according to the pyproject.toml file
lint                 Run code formatters and linter
fix-code-style       Fix code formatting
tox-listenvs         List all tox test environments
tox                  Run pytest via tox with all environments
tox-py36             Run pytest via tox with *python v3.6*
tox-py37             Run pytest via tox with *python v3.7*
tox-py38             Run pytest via tox with *python v3.8*
tox-py39             Run pytest via tox with *python v3.9*
pytest               Run pytest
pytest-ci            Run pytest with CI settings
publish              Release new version to PyPi
makemessages         Make and compile locales message files
```

# License

[MIT](LICENSE)
