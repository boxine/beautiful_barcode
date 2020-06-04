# beautiful_barcode
Generate well-formatted, production-ready Barcodes.

By default, existing Python barcode libraries like [python-barcode](https://pypi.org/project/python-barcode/) generate good barcodes, but any and all formatting of the text is left up to the user. beautiful_barcode generates a nicely formatted barcode with interleaved text out of the box:

![Example barcode](example_path.svg)

Depending on your renderer (and true by default), text in the barcode is *not* an SVG `<text>` element, as such an elment may render differently on different machines depending on font availability.

This library is currently limited to UPC-A and SVG – that's all we (the original authors) needed. Patches welcome!

# Installation

```sh
$ pip install beautiful_barcode
```

# Usage

```
>>> from beautiful_barcode import UPCA
>>> UPCA('012345678905').write('output.svg')
```

Command line:

```sh
$ python -m beautiful_barcode 012345678905 -o output.svg
```

# License

[MIT](LICENSE)
