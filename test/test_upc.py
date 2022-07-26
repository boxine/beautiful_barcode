import unittest
from pathlib import Path

import beautiful_barcode
from beautiful_barcode import UPCA, InvalidGTIN


BASE_PATH = Path(beautiful_barcode.__file__).parent.parent


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


class PathSVGRendererTest(unittest.TestCase):
    def test_render_svg(self):
        svg = UPCA('012345678905').render(renderer='path')
        assert b'<svg version="1.1"' in svg
        assert b'</svg>' in svg

        reference_file = Path(BASE_PATH, 'example_path.svg')
        assert reference_file.is_file()

        reference = reference_file.read_bytes()
        if reference != svg:
            # Just "update" the example file for easy commit a new version
            # And you can also see the difference via git ;)
            reference_file.write_bytes(svg)

            assert reference == svg
