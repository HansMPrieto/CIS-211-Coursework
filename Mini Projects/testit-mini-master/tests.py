"""Hans Prieto
Test It Mini-Project
Unit tests for testme.py
"""

import unittest
from buggy import *

class TestMaxRun(unittest.TestCase):
    """Tests the function max_run and checks
    if it produces expected results."""
    def test_max_run_example(self):
        self.assertEqual(max_run([1, 2, 2, 2, 3]), [2, 2, 2])

    def test_max_run_example2(self):
        """test for empty list"""
        self.assertEqual(max_run([]), [])

    def test_max_run_example3(self):
        """test for same element"""
        self.assertEqual(max_run([1, 1, 1]), [1, 1, 1])

    def test_max_run_example4(self):
        self.assertEqual(max_run([1, 1, 2, 3]), [1, 1])

    def test_max_run_example5(self):
        self.assertEqual(max_run([1, 1, 2, 3, 3, 3, 3]), [3, 3, 3, 3])

    def test_max_run_example6(self):
        self.assertEqual(max_run([1, 1, 2, 2, 3, 4]), [1, 1])

if __name__ == "__main__":
    unittest.main()
