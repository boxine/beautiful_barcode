__version__ = '1.1.3'

from .ean import EAN  # noqa
from .exceptions import InvalidGTIN
from .upc import UPCA  # noqa


def GTIN(gtin):
    length = len(gtin)
    if length == 12:
        return UPCA(gtin)
    elif length == 13:
        return EAN(gtin)
    else:
        raise InvalidGTIN(f'Unsupported GTIN {gtin!r} of length {length}')
