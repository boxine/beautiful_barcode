import unittest

import tutils  # noqa
from beautiful_barcode import UPCA


class UPCTest(unittest.TestCase):
    def test_upc_modules(self):
        self.assertEqual(
            UPCA('012345012345').to_modules(),
            ('101  0001101 0011001 0010011 0111101 0100011 0110001  01010'
             '     1110010 1100110 1101100 1000010 1011100 1001110  101')
            .replace(' ', '')
        )

        self.assertEqual(
            UPCA('567890567890').to_modules(),
            ('101  0110001 0101111 0111011 0110111 0001011 0001101  01010'
             '     1001110 1010000 1000100 1001000 1110100 1110010  101')
            .replace(' ', '')
        )
