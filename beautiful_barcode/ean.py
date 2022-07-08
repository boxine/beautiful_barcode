import re

from .barcode import Barcode
from .utils import module_coords


# noqa See https://en.wikipedia.org/wiki/International_Article_Number#Binary_encoding_of_data_digits_into_EAN-13_barcode
_START_END = '101'
_MIDDLE = '01010'
_L_DIGITS = (
    '0001101', '0011001', '0010011', '0111101', '0100011',
    '0110001', '0101111', '0111011', '0110111', '0001011',
)
_G_DIGITS = (
    '0100111', '0110011', '0011011', '0100001', '0011101',
    '0111001', '0000101', '0010001', '0001001', '0010111',
)
_DIGITS_BY_GROUP = {'L': _L_DIGITS, 'G': _G_DIGITS}
_GROUPS_BY_FIRST_DIGIT = (
    'LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG',
    'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL',
)
_R_DIGITS = (
    '1110010', '1100110', '1101100', '1000010', '1011100',
    '1001110', '1010000', '1000100', '1001000', '1110100',
)
_EAN_MODULE_COUNT = 95


def calc_ean_checksum(ean):
    return (- sum(
        (1 if pos % 2 == 0 else 3) * num
        for pos, num in enumerate(map(int, ean[:-1])))) % 10


class EAN(Barcode):
    def __init__(self, ean: str):
        super().__init__()

        assert isinstance(ean, str)
        if not re.match(r'^[0-9]{13}$', ean):
            raise ValueError(f'EAN {ean!r} is not 13 latin digits')
        checksum = calc_ean_checksum(ean)
        if checksum != int(ean[-1]):
            raise ValueError(f'EAN checksum of {ean} should be {checksum}')

        self.ean = ean

    def to_modules(self):
        groups = _GROUPS_BY_FIRST_DIGIT[int(self.ean[0])]

        res = (
            _START_END +
            ''.join(_DIGITS_BY_GROUP[group][int(c)] for c, group in zip(self.ean[1:7], groups)) +
            _MIDDLE +
            ''.join(_R_DIGITS[int(c)] for c in self.ean[7:]) +
            _START_END
        )
        assert len(res) == _EAN_MODULE_COUNT
        return res

    def _paint(self, renderer):
        MODULE_WIDTH = 2
        MODULE_HEIGHT_SMALL = 75
        MODULE_HEIGHT = 90
        QUIET_ZONE = 9
        WIDTH = (QUIET_ZONE + _EAN_MODULE_COUNT + QUIET_ZONE) * MODULE_WIDTH
        HEIGHT = 100

        renderer.initialize(WIDTH, HEIGHT)
        for left, width in module_coords(self.to_modules()):
            use_large_module = (
                (left + width <= 3) or
                (left >= 45 and left < 50) or
                left >= 92
            )
            renderer.rect(
                x=(left + QUIET_ZONE) * MODULE_WIDTH,
                y=0,
                width=width * MODULE_WIDTH,
                height=(MODULE_HEIGHT if use_large_module else MODULE_HEIGHT_SMALL)
            )

        # Write human-readable EAN
        TEXT_Y = 95
        TEXT_SCALE = 1.18  # slightly larger font (since EAN blocks less space than UPC)
        renderer.text(self.ean[:1], x=3, y=TEXT_Y, scale=TEXT_SCALE)
        renderer.text(self.ean[1:7], x=24, y=TEXT_Y, scale=TEXT_SCALE)
        renderer.text(self.ean[7:], x=117, y=TEXT_Y, scale=TEXT_SCALE)
