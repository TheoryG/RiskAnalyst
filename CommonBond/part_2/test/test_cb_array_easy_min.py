"""
Unittests for CBArrayEasyMin.
"""

import unittest
from unittest import TestCase
from src.cb_array_easy_min import CBArrayEasyMin


class TestCBArrayEasyMin(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_get_min(self):
        arr = CBArrayEasyMin([])
        self.assertIsNone(arr.get_min())

    def test_002_get_min(self):
        arr = CBArrayEasyMin([], dtype=float)
        self.assertIsNone(arr.get_min())

    def test_003_get_min(self):
        arr = CBArrayEasyMin([], dtype=str)
        self.assertIsNone(arr.get_min())

    def test_004_get_min(self):
        arr = CBArrayEasyMin([1])
        self.assertEqual(arr.get_min(), 1)

    def test_005_get_min(self):
        arr = CBArrayEasyMin([1.5])
        self.assertEqual(arr.get_min(), 1.5)

    def test_006_get_min(self):
        arr = CBArrayEasyMin(['hi'])
        self.assertEqual(arr.get_min(), 'hi')

    def test_007_get_min(self):
        arr = CBArrayEasyMin([2, 1, 1])
        self.assertEqual(arr.get_min(), 1)

    def test_008_get_min(self):
        arr = CBArrayEasyMin(['b', 'c'])
        self.assertEqual(arr.get_min(), 'b')

    def test_009_get_min(self):
        arr = CBArrayEasyMin([5.5, 5.5])
        self.assertEqual(arr.get_min(), 5.5)

    def test_010_get_min(self):
        arr = CBArrayEasyMin([1])
        self.assertEqual(arr.get_min(), 1)

    def test_011_get_min(self):
        arr = CBArrayEasyMin([1])
        arr.append(2)
        self.assertEqual(arr.get_min(), 1)
        arr.append(0)
        self.assertEqual(arr.get_min(), 0)

    def test_012_get_min(self):
        arr = CBArrayEasyMin([1])
        arr.insert(0, 2)
        self.assertEqual(arr.get_min(), 1)
        arr.insert(0, 0)
        self.assertEqual(arr.get_min(), 0)

    def test_013_get_min(self):
        arr = CBArrayEasyMin([1])
        arr.insert(0, 2)
        self.assertEqual(arr.get_min(), 1)
        arr.insert(0, 0)
        self.assertEqual(arr.get_min(), 0)
        arr.remove(1)
        self.assertEqual(arr.get_min(), 0)
        arr.remove(0)
        self.assertEqual(arr.get_min(), 2)
        arr.append(-1)
        self.assertEqual(arr.get_min(), -1)
        arr.append(-1)
        self.assertEqual(arr.get_min(), -1)
        arr.remove_all(-1)
        self.assertEqual(arr.get_min(), 2)

if __name__ == '__main__':
    unittest.main()
