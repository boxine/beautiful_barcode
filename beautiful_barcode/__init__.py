__version__ = '1.1.0'

from .ean import EAN  # noqa
from .upc import UPCA  # noqa


def gtin(value):
    length = len(value)
    if length == 12:
        return UPCA(value)
    elif length == 13:
        return EAN(value)
    else:
        raise ValueError(f'Unsupported GTIN {gtin!r} of length {length}')
