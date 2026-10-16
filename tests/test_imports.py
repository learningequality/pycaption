from __future__ import unicode_literals

import subprocess
import sys
import unittest


class ImportTestCase(unittest.TestCase):
    def test_import_does_not_load_future_or_tkinter(self):
        # future.backports pulls in tkinter, whose Tcl fork handler can hang
        # subprocess calls in the importing process on macOS.
        code = (
            "import sys, pycaption; "
            "print(' '.join(sorted(m for m in sys.modules "
            "if m.split('.')[0] in ('future', 'past', 'tkinter', 'Tkinter'))))"
        )
        output = subprocess.check_output([sys.executable, "-c", code])
        self.assertEqual(output.decode("utf-8").strip(), "")
