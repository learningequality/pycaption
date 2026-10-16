from __future__ import unicode_literals
import unittest

from pycaption import DFXPReader
from pycaption.base import merge_concurrent_captions
from pycaption.utils import classic_div
from .samples.dfxp import DFXP_WITH_CONCURRENT_CAPTIONS


class FunctionsTestCase(unittest.TestCase):

    def test_merge_concurrent_captions(self):
        caption_set = DFXPReader().read(DFXP_WITH_CONCURRENT_CAPTIONS)
        captions = caption_set.get_captions('en-US')
        self.assertEqual(len(captions), 5)

        caption_set = merge_concurrent_captions(caption_set)
        captions = caption_set.get_captions('en-US')
        self.assertEqual(len(captions), 3)

    def test_classic_div(self):
        self.assertEqual(classic_div(1500, 1000), 1)
        self.assertEqual(classic_div(1500.0, 1000), 1.5)
        self.assertEqual(classic_div(25, 2), 12)
        self.assertEqual(classic_div(25.0, 2), 12.5)
