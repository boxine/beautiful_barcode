__version__ = '1.1.2'

from .ean import EAN  # noqa
from .upc import UPCA  # noqa


def GTIN(gtin):
    length = len(gtin)
    if length == 12:
        return UPCA(gtin)
    elif length == 13:
        return EAN(gtin)
    else:
        raise ValueError(f'Unsupported GTIN {gtin!r} of length {length}')
