import unittest

import tutils  # noqa
from beautiful_barcode.utils import module_coords


class UtilsTest(unittest.TestCase):
    def test_module_coords(self):
        modules = ('101  0001101 0011001 0010011 0111101 0100011 0110001  01010'
                   '     1110010 1100110 1101100 1000010 1011100 1001110  101'.replace(' ', ''))

        self.assertEqual(
            list(module_coords(modules)),
            [(0, 1), (2, 1), (6, 2), (9, 1), (12, 2), (16, 1), (19, 1), (22, 2),
             (25, 4), (30, 1), (32, 1), (36, 2), (39, 2), (44, 1), (46, 1), (48, 1),
             # second row in test_upc_modules (starting with right digits)
             (50, 3), (55, 1), (57, 2), (61, 2), (64, 2), (67, 2), (71, 1), (76, 1), (78, 1),
             (80, 3), (85, 1), (88, 3), (92, 1), (94, 1)]
        )
