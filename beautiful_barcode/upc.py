import re

from .barcode import Barcode
from .utils import module_coords


# See https://en.wikipedia.org/wiki/Universal_Product_Code#Encoding
_START_END = '101'
_MIDDLE = '01010'
_LEFT = (
    '0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011',
    '0110111', '0001011',
)
_RIGHT = (
    '1110010', '1100110', '1101100', '1000010', '1011100', '1001110', '1010000', '1000100',
    '1001000', '1110100',
)
_UPC_MODULE_COUNT = 95


def calc_upc_checksum(upc):
    return (- sum(
        (3 if pos % 2 == 0 else 1) * num
        for pos, num in enumerate(map(int, upc[:-1])))) % 10


class UPCA(Barcode):
    def __init__(self, upc: str):
        super().__init__()

        assert isinstance(upc, str)
        if not re.match(r'^[0-9]{12}$', upc):
            raise ValueError(f'UPC {upc!r} is not 12 latin digits')
        upc_checksum = calc_upc_checksum(upc)
        if upc_checksum != int(upc[-1]):
            raise ValueError(f'UPC checksum of {upc} should be {upc_checksum}')

        self.upc = upc

    def to_modules(self):
        res = (
            _START_END +
            ''.join(_LEFT[int(c)] for c in self.upc[:6]) +
            _MIDDLE +
            ''.join(_RIGHT[int(c)] for c in self.upc[6:]) +
            _START_END
        )
        assert len(res) == _UPC_MODULE_COUNT
        return res

    def _paint(self, renderer):
        MODULE_WIDTH = 2
        MODULE_HEIGHT_SMALL = 75
        MODULE_HEIGHT = 90
        QUIET_ZONE = 9
        WIDTH = (QUIET_ZONE + _UPC_MODULE_COUNT + QUIET_ZONE) * MODULE_WIDTH
        HEIGHT = 100

        renderer.initialize(WIDTH, HEIGHT)
        for left, width in module_coords(self.to_modules()):
            use_large_module = (
                (left + width < 11) or
                (left > 45 and left + width < 50) or
                left > 84
            )
            renderer.rect(
                x=(left + QUIET_ZONE) * MODULE_WIDTH,
                y=0,
                width=width * MODULE_WIDTH,
                height=(MODULE_HEIGHT if use_large_module else MODULE_HEIGHT_SMALL)
            )

        # Write human-readable UPC
        TEXT_Y = 95
        renderer.text(self.upc[:1], x=3, y=TEXT_Y)
        renderer.text(self.upc[1:6], x=44, y=TEXT_Y)
        renderer.text(self.upc[6:11], x=123, y=TEXT_Y)
        renderer.text(self.upc[11:], x=212, y=TEXT_Y)
