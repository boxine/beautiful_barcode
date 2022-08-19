import unittest

import tutils  # noqa
from beautiful_barcode.renderers import make_renderer, InkscapeEPSRenderer


class RendererTest(unittest.TestCase):
    def test_auto_eps(self):
        svg_renderer = make_renderer('auto', extension='.svg')
        self.assertFalse(isinstance(svg_renderer, InkscapeEPSRenderer))  # actual result is implementation-defined

        eps_renderer = make_renderer('auto', extension='.eps')
        self.assertTrue(isinstance(eps_renderer, InkscapeEPSRenderer))
