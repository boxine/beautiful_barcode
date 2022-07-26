import unittest

import tutils  # noqa
from beautiful_barcode import EAN, InvalidGTIN
from beautiful_barcode.ean import _L_DIGITS, _G_DIGITS, _R_DIGITS


class EANTest(unittest.TestCase):
    def test_digit_properties(self):
        for digit, (l, g, r) in enumerate(zip(_L_DIGITS, _G_DIGITS, _R_DIGITS)):
            self.assertEqual(
                g[::-1], r, f'G digits {g} should be reverse of R digits {r} for digit {digit}')

            negated_l = f'{(~ int(l, 2)) % 128:b}'
            self.assertEqual(
                negated_l, r,
                f'L digits {l} should be bitwise negation of R digits {r} for digit {digit}')

    def test_ean_modules(self):
        self.assertEqual(
            EAN('0567890567896').to_modules(),
            ('101  0110001 0101111 0111011 0110111 0001011 0001101  01010'
             '     1001110 1010000 1000100 1001000 1110100 1010000  101')
            .replace(' ', '')
        )

        self.assertEqual(
            EAN('4251192109019').to_modules(),
            ('101  0010011 0111001 0011001 0011001 0010111 0011011  01010'
             '     1100110 1110010 1110100 1110010 1100110 1110100  101')
            .replace(' ', '')
        )

        self.assertEqual(
            EAN('5901234123457').to_modules(),
            ('101  0001011 0100111 0110011 0010011 0111101 0011101  01010'
             '     1100110 1101100 1000010 1011100 1001110 1000100  101')
            .replace(' ', '')
        )

    def test_checksum(self):
        with self.assertRaisesRegex(InvalidGTIN, r'EAN \'56789056789\' is not 13 latin digits'):
            EAN('56789056789')
        with self.assertRaisesRegex(InvalidGTIN, r'EAN \'567890567890\' is not 13 latin digits'):
            EAN('567890567890')
        with self.assertRaisesRegex(InvalidGTIN, r'EAN checksum of 5678905678967 should be 6'):
            EAN('5678905678967')
        with self.assertRaisesRegex(InvalidGTIN, r'EAN checksum of 4251192107550 should be 8'):
            EAN('4251192107550')
        with self.assertRaisesRegex(InvalidGTIN, r'EAN checksum of 1222222222222 should be 3'):
            EAN('1222222222222')

