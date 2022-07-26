import unittest

import tutils  # noqa
from beautiful_barcode import InvalidGTIN, UPCA


class UPCTest(unittest.TestCase):
    def test_upc_modules(self):
        self.assertEqual(
            UPCA('012345012341').to_modules(),
            ('101  0001101 0011001 0010011 0111101 0100011 0110001  01010'
             '     1110010 1100110 1101100 1000010 1011100 1100110  101')
            .replace(' ', '')
        )

        self.assertEqual(
            UPCA('567890567896').to_modules(),
            ('101  0110001 0101111 0111011 0110111 0001011 0001101  01010'
             '     1001110 1010000 1000100 1001000 1110100 1010000  101')
            .replace(' ', '')
        )

    def test_checksum(self):
        with self.assertRaisesRegex(InvalidGTIN, r'UPC \'12345678901\' is not 12 latin digits'):
            UPCA('12345678901')
        with self.assertRaisesRegex(InvalidGTIN, r'UPC \'12345678901a\' is not 12 latin digits'):
            UPCA('12345678901a')
        with self.assertRaisesRegex(InvalidGTIN, r'UPC checksum of 123456789013 should be 2'):
            UPCA('123456789013')
