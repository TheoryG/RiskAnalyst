"""
Unittests for CBArray and CBArrayEasyMin.
"""

import unittest
from unittest import TestCase
from src.cb_array import CBArray
from src.cb_array_easy_min import CBArrayEasyMin


class TestCBArray(TestCase):

    def setUp(self):
        self._classes = [CBArray, CBArrayEasyMin]

    def tearDown(self):
        del self._classes

    def test_001_constructor(self):
        for cls in self._classes:
            arr = cls([])
            self.assertIsNotNone(arr)
            self.assertEqual(arr.dtype, int)
            self.assertEqual(arr.size, 0)

    def test_002_constructor(self):
        for cls in self._classes:
            arr = cls([3])
            self.assertIsNotNone(arr)
            self.assertEqual(arr.dtype, int)
            self.assertEqual(arr.size, 1)

    def test_003_constructor(self):
        for cls in self._classes:
            arr = cls([1.5, 2.5, 3.0])
            self.assertIsNotNone(arr)
            self.assertEqual(arr.dtype, float)
            self.assertEqual(arr.size, 3)

    def test_004_constructor(self):
        for cls in self._classes:
            arr = cls([1, 2.5, 3])
            self.assertIsNotNone(arr)
            self.assertEqual(arr.dtype, float)
            self.assertEqual(arr.size, 3)

    def test_005_constructor(self):
        for cls in self._classes:
            arr = cls([1, 2, 3])
            self.assertIsNotNone(arr)
            self.assertEqual(arr.dtype, int)
            self.assertEqual(arr.size, 3)

    def test_006_constructor(self):
        for cls in self._classes:
            arr = cls(['cb'])
            self.assertIsNotNone(arr)
            self.assertEqual(arr.dtype, str)
            self.assertEqual(arr.size, 1)

    def test_007_constructor(self):
        for cls in self._classes:
            arr = cls(['c', 'o', 'm', 'm', 'o', 'n', 'b', 'o', 'n', 'd'])
            self.assertIsNotNone(arr)
            self.assertEqual(arr.dtype, str)
            self.assertEqual(arr.size, 10)

    def test_008_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls(['h', 1])

    def test_009_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls(['h', 1.5])

    def test_010_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls([complex(0, 1)])  # Unsupported data type

    def test_011_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls([1, cls([2])])

    def test_012_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls(None)

    def test_013_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls(1)

    def test_014_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls(1.5)

    def test_015_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls('hi')

    def test_016_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls()

    def test_017_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls([1, 2, None])

    def test_018_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls([None])

    def test_019_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls([1.5, None, 2.5])

    def test_020_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls([None, 'hello'])

    def test_021_constructor(self):
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls([None, None, None])

    def test_022_constructor(self):
        for cls in self._classes:
            arr = cls([1, 2], dtype=float)
            self.assertEqual(arr.dtype, float)
            self.assertEqual(arr.size, 2)

    def test_023_constructor(self):
        for cls in self._classes:
            arr = cls([1.0, 2.5], dtype=float)
            self.assertEqual(arr.dtype, float)
            self.assertEqual(arr.size, 2)

    def test_024_constructor(self):
        for cls in self._classes:
            arr = cls([], dtype=int)
            self.assertEqual(arr.dtype, int)
            self.assertEqual(arr.size, 0)

    def test_025_constructor(self):
        for cls in self._classes:
            arr = cls([], dtype=float)
            self.assertEqual(arr.dtype, float)
            self.assertEqual(arr.size, 0)

    def test_026_constructor(self):
        for cls in self._classes:
            arr = cls([], dtype=str)
            self.assertEqual(arr.dtype, str)
            self.assertEqual(arr.size, 0)

    def test_027_constructor(self):
        for cls in self._classes:
            arr = cls(['hello', 'commonbond'], dtype=str)
            self.assertEqual(arr.dtype, str)
            self.assertEqual(arr.size, 2)

    def test_028_constructor(self):
        """
        Implicit conversion from float to int (Down-casting).
        """
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls([1.0, 2.5], dtype=int)

    def test_029_constructor(self):
        """
        Implicit conversion from float to str.
        """
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls([1.0, 2.5], dtype=str)

    def test_030_constructor(self):
        """
        Implicit conversion from int to str.
        """
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls([1, 2], dtype=str)

    def test_031_constructor(self):
        """
        Implicit conversion from str to int.
        """
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls(['1', '2'], dtype=int)

    def test_032_constructor(self):
        """
        Implicit conversion from str to float.
        """
        for cls in self._classes:
            with self.assertRaises(Exception):
                _ = cls(['1.5', '2.3'], dtype=float)

    def test_033_append(self):
        for cls in self._classes:
            arr = cls([])
            arr.append(3)
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 3)
            self.assertEqual(arr[-1], 3)

    def test_034_append(self):
        for cls in self._classes:
            arr = cls([1, 2], dtype=float)
            arr.append(3)
            self.assertEqual(arr.size, 3)
            self.assertEqual(arr[2], 3)
            self.assertEqual(arr[-1], 3)

    def test_035_append(self):
        for cls in self._classes:
            arr = cls([1.0, 2])
            arr.append(3)
            self.assertEqual(arr.size, 3)
            self.assertEqual(arr[2], 3)
            self.assertEqual(arr[-1], 3)

    def test_036_append(self):
        for cls in self._classes:
            arr = cls([1.0, 2])
            arr.append(3)
            self.assertEqual(arr.size, 3)
            self.assertEqual(arr[2], 3)
            self.assertEqual(arr[-1], 3)

    def test_037_append(self):
        for cls in self._classes:
            arr = cls([1.0, 2])
            arr.append(3)
            self.assertEqual(arr.size, 3)
            self.assertEqual(arr[2], 3)
            self.assertEqual(arr[-1], 3)

    def test_038_append(self):
        for cls in self._classes:
            arr = cls([1.0, 2])
            arr.append(3)
            self.assertEqual(arr.size, 3)
            self.assertEqual(arr[2], 3)
            self.assertEqual(arr[-1], 3)

    def test_039_append(self):
        for cls in self._classes:
            arr = cls([1.0, 2])
            arr.append(3)
            self.assertEqual(arr.size, 3)
            self.assertEqual(arr[2], 3)
            self.assertEqual(arr[-1], 3)

    def test_040_append(self):
        for cls in self._classes:
            arr = cls([])
            for i in range(100):
                arr.append(i)
            self.assertEqual(arr.dtype, int)
            self.assertEqual(arr.size, 100)
            self.assertEqual(arr[50], 50)
            self.assertEqual(arr[-1], 99)

    def test_041_append(self):
        """
        Implicit conversion from float to int (Down-casting)
        """
        for cls in self._classes:
            arr = cls([])
            with self.assertRaises(Exception):
                arr.append(3.5)

    def test_042_append(self):
        """
        Implicit conversion from float to str.
        """
        for cls in self._classes:
            arr = cls([], dtype=float)
            with self.assertRaises(Exception):
                arr.append('3.5')

    def test_043_append(self):
        """
        Implicit conversion from int to str.
        """
        for cls in self._classes:
            arr = cls([], dtype=int)
            with self.assertRaises(Exception):
                arr.append('3.5')

    def test_044_append(self):
        """
        Implicit conversion from str to float.
        """
        for cls in self._classes:
            arr = cls([], dtype=str)
            with self.assertRaises(Exception):
                arr.append(3.5)

    def test_045_append(self):
        """
        Implicit conversion from str to int.
        """
        for cls in self._classes:
            arr = cls([], dtype=str)
            with self.assertRaises(Exception):
                arr.append(3)

    def test_046_append(self):
        """
        Unsupported data type.
        """
        for cls in self._classes:
            arr = cls([])
            with self.assertRaises(Exception):
                arr.append(complex(1, 2))

    def test_047_insert(self):
        for cls in self._classes:
            arr = cls([])
            arr.insert(0, 3)
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 3)
            self.assertEqual(arr[-1], 3)

    def test_048_insert(self):
        for cls in self._classes:
            arr = cls([5.6])
            arr.insert(1, 3)
            self.assertEqual(arr.size, 2)
            self.assertEqual(arr[0], 5.6)
            self.assertEqual(arr[-1], 3)

    def test_049_insert(self):
        for cls in self._classes:
            arr = cls([5.6, 7.8])
            arr.insert(1, 3)
            self.assertEqual(arr.size, 3)
            self.assertEqual(arr[1], 3)

    def test_050_insert(self):
        for cls in self._classes:
            arr = cls([5.6, 7.8])
            arr.insert(2, 3)
            self.assertEqual(arr.size, 3)
            self.assertEqual(arr[-1], 3)

    def test_051_insert(self):
        for cls in self._classes:
            arr = cls([])
            with self.assertRaises(Exception):
                arr.insert(1, 3)

    def test_052_insert(self):
        for cls in self._classes:
            arr = cls([5.6, 7.8])
            with self.assertRaises(Exception):
                arr.insert(3, 3)

    def test_053_insert(self):
        for cls in self._classes:
            arr = cls([5.6, 7.8])
            with self.assertRaises(Exception):
                arr.insert(-1, 3)

    def test_054_insert(self):
        for cls in self._classes:
            arr = cls([])
            with self.assertRaises(Exception):
                arr.insert(0, None)

    def test_055_insert(self):
        for cls in self._classes:
            arr = cls(['commonbond'])
            with self.assertRaises(Exception):
                arr.insert(0, None)

    def test_056_insert(self):
        """
        Implicit conversion from float to int (Down-casting)
        """
        for cls in self._classes:
            arr = cls([])
            with self.assertRaises(Exception):
                arr.insert(0, 3.5)

    def test_057_insert(self):
        """
        Implicit conversion from str to int
        """
        for cls in self._classes:
            arr = cls([])
            with self.assertRaises(Exception):
                arr.insert(0, 'commonbond')

    def test_058_insert(self):
        """
        Implicit conversion from str to float
        """
        for cls in self._classes:
            arr = cls([0.5])
            with self.assertRaises(Exception):
                arr.insert(0, 'commonbond')

    def test_059_insert(self):
        """
        Implicit conversion from float to str
        """
        for cls in self._classes:
            arr = cls(['comonbond'])
            with self.assertRaises(Exception):
                arr.insert(0, 6.6)

    def test_060_insert(self):
        """
        Implicit conversion from int to str
        """
        for cls in self._classes:
            arr = cls(['comonbond'])
            with self.assertRaises(Exception):
                arr.insert(0, 5)

    def test_061_insert(self):
        """
        Implicit conversion from int to str
        """
        for cls in self._classes:
            arr = cls(['comonbond'])
            with self.assertRaises(Exception):
                arr.insert(0, 5)

    def test_062_insert(self):
        """
        Unsupported data type.
        """
        for cls in self._classes:
            arr = cls(['comonbond'])
            with self.assertRaises(Exception):
                arr.insert(0, complex(1, 1))

    def test_063_remove(self):
        for cls in self._classes:
            arr = cls([])
            arr.remove(1)
            self.assertEqual(arr.size, 0)

    def test_064_remove(self):
        for cls in self._classes:
            arr = cls([1])
            arr.remove(1)
            self.assertEqual(arr.size, 0)

    def test_065_remove(self):
        for cls in self._classes:
            arr = cls([1])
            arr.remove(2)
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 1)

    def test_066_remove(self):
        for cls in self._classes:
            arr = cls([1, 2])
            arr.remove(1)
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 2)

    def test_067_remove(self):
        for cls in self._classes:
            arr = cls([2, 1])
            arr.remove(1)
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 2)

    def test_068_remove(self):
        for cls in self._classes:
            arr = cls([2.5, 1, 2.5])
            arr.remove(2.5)
            self.assertEqual(arr.size, 2)
            self.assertEqual(arr[0], 1)
            self.assertEqual(arr[1], 2.5)

    def test_069_remove(self):
        for cls in self._classes:
            arr = cls(['c', 'o', 'm', 'm', 'o', 'n', 'b', 'o', 'n', 'd'])
            arr.remove('m')
            self.assertEqual(arr.size, 9)
            self.assertEqual(arr[2], 'm')
            self.assertEqual(arr[3], 'o')

    def test_070_remove(self):
        for cls in self._classes:
            arr = cls([1.0])
            arr.remove(1)
            self.assertEqual(arr.size, 0)

    def test_071_remove(self):
        """
        Implicit conversion from float to int (Down-casting)
        """
        for cls in self._classes:
            arr = cls([])
            with self.assertRaises(Exception):
                arr.remove(3.5)

    def test_072_remove(self):
        """
        Implicit conversion from float to int (Down-casting)
        """
        for cls in self._classes:
            arr = cls([2])
            with self.assertRaises(Exception):
                arr.remove(2.0)

    def test_073_remove(self):
        """
        Implicit conversion from str to int
        """
        for cls in self._classes:
            arr = cls([2])
            with self.assertRaises(Exception):
                arr.remove('commonbond')

    def test_074_remove(self):
        """
        Implicit conversion from str to float
        """
        for cls in self._classes:
            arr = cls([2.5])
            with self.assertRaises(Exception):
                arr.remove('commonbond')

    def test_075_remove(self):
        """
        Implicit conversion from str to float
        """
        for cls in self._classes:
            arr = cls([2.5])
            with self.assertRaises(Exception):
                arr.remove('commonbond')

    def test_076_remove(self):
        """
        Implicit conversion from float to str
        """
        for cls in self._classes:
            arr = cls(['commonbond'])
            with self.assertRaises(Exception):
                arr.remove(2.5)

    def test_077_remove(self):
        """
        Implicit conversion from int to str
        """
        for cls in self._classes:
            arr = cls(['commonbond'])
            with self.assertRaises(Exception):
                arr.remove(2)

    def test_078_remove_all(self):
        for cls in self._classes:
            arr = cls([])
            arr.remove_all(2)
            self.assertEqual(arr.size, 0)

    def test_079_remove_all(self):
        for cls in self._classes:
            arr = cls([2, 2, 2])
            arr.remove_all(2)
            self.assertEqual(arr.size, 0)

    def test_080_remove_all(self):
        for cls in self._classes:
            arr = cls([2, 1, 2])
            arr.remove_all(2)
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 1)

    def test_081_remove_all(self):
        for cls in self._classes:
            arr = cls([1, 2])
            arr.remove_all(2)
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 1)

    def test_082_remove_all(self):
        for cls in self._classes:
            arr = cls([1.5, 2.0])
            arr.remove_all(2)
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 1.5)

    def test_083_remove_all(self):
        for cls in self._classes:
            arr = cls(['hi', 'commonbond', 'hi'])
            arr.remove_all('hi')
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 'commonbond')

    def test_084_remove_all(self):
        """
        Implicit conversion from float to int (Down-casting)
        """
        for cls in self._classes:
            arr = cls([])
            with self.assertRaises(Exception):
                arr.remove_all(3.5)

    def test_085_remove_all(self):
        """
        Implicit conversion from str to int
        """
        for cls in self._classes:
            arr = cls([])
            with self.assertRaises(Exception):
                arr.remove_all('commonbond')

    def test_086_remove_all(self):
        """
        Implicit conversion from float to str
        """
        for cls in self._classes:
            arr = cls(['hello'])
            with self.assertRaises(Exception):
                arr.remove_all(3.5)

    def test_087_remove_all(self):
        """
        Implicit conversion from int to str
        """
        for cls in self._classes:
            arr = cls(['hello'])
            with self.assertRaises(Exception):
                arr.remove_all(3)

    def test_088_remove_all(self):
        """
        Implicit conversion from str to int
        """
        for cls in self._classes:
            arr = cls([])
            with self.assertRaises(Exception):
                arr.remove_all('hi!')

    def test_089_remove_all(self):
        """
        Implicit conversion from str to int
        """
        for cls in self._classes:
            arr = cls([3.5])
            with self.assertRaises(Exception):
                arr.remove_all('hi!')

    def test_090_remove_all(self):
        """
        Unsupported data type.
        """
        for cls in self._classes:
            arr = cls([])
            with self.assertRaises(Exception):
                arr.remove_all(complex(1, 1))

    def test_091_concatenation(self):
        for cls in self._classes:
            arr1 = cls([])
            arr2 = cls([])
            arr = arr1 + arr2
            self.assertEqual(arr.size, 0)

    def test_092_concatenation(self):
        for cls in self._classes:
            arr1 = cls([])
            arr2 = cls([1])
            arr = arr1 + arr2
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 1)

    def test_093_concatenation(self):
        for cls in self._classes:
            arr1 = cls([])
            arr2 = cls([1.5])
            arr = arr1 + arr2
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 1.5)
            self.assertEqual(arr.dtype, float)

    def test_094_concatenation(self):
        for cls in self._classes:
            arr1 = cls([], dtype=str)
            arr2 = cls(['commonbond'])
            arr = arr1 + arr2
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 'commonbond')
            self.assertEqual(arr.dtype, str)

    def test_095_concatenation(self):
        for cls in self._classes:
            arr1 = cls([2.6])
            arr2 = cls([])
            arr = arr1 + arr2
            self.assertEqual(arr.size, 1)
            self.assertEqual(arr[0], 2.6)
            self.assertEqual(arr.dtype, float)

    def test_096_concatenation(self):
        for cls in self._classes:
            arr1 = cls([2.6])
            arr2 = cls([5.2])
            arr = arr1 + arr2
            self.assertEqual(arr.size, 2)
            self.assertEqual(arr[-1], 5.2)
            self.assertEqual(arr.dtype, float)

    def test_097_concatenation(self):
        for cls in self._classes:
            arr1 = cls([2])
            arr2 = cls([5.2])
            arr = arr1 + arr2
            self.assertEqual(arr.size, 2)
            self.assertEqual(arr[-1], 5.2)
            self.assertEqual(arr.dtype, float)

    def test_098_concatenation(self):
        for cls in self._classes:
            arr1 = cls([2.5])
            arr2 = cls([5])
            arr = arr1 + arr2
            self.assertEqual(arr.size, 2)
            self.assertEqual(arr[-1], 5)
            self.assertEqual(arr.dtype, float)

    def test_099_concatenation(self):
        for cls in self._classes:
            arr1 = cls([2] * 5)
            arr2 = cls([5.2] * 10)
            arr = arr1 + arr2
            self.assertEqual(arr.size, 15)
            self.assertEqual(arr[-1], 5.2)
            self.assertEqual(arr.dtype, float)

    def test_100_concatenation(self):
        for cls in self._classes:
            arr1 = cls(['hi'])
            arr2 = cls([5.2])
            with self.assertRaises(Exception):
                _ = arr1 + arr2

    def test_101_concatenation(self):
        for cls in self._classes:
            arr1 = cls(['hi'])
            arr2 = cls([5])
            with self.assertRaises(Exception):
                _ = arr1 + arr2

    def test_102_concatenation(self):
        for cls in self._classes:
            arr1 = cls([5])
            arr2 = cls(['hello'])
            with self.assertRaises(Exception):
                _ = arr1 + arr2

    def test_103_concatenation(self):
        for cls in self._classes:
            arr1 = cls([5.6])
            arr2 = cls(['hello'])
            with self.assertRaises(Exception):
                _ = arr1 + arr2

    def test_104_concatenation(self):
        for cls in self._classes:
            arr1 = cls([5.6])
            arr = arr1 + arr1
            self.assertEqual(arr.size, 2)
            self.assertEqual(arr[0], 5.6)
            self.assertEqual(arr[-1], 5.6)

    def test_105_concatenation(self):
        for cls in self._classes:
            arr1 = cls([5.6] * 2)
            arr2 = cls([2])
            arr3 = cls([5.8])
            arr = arr1 + arr2 + arr3
            self.assertEqual(arr.size, 4)
            self.assertEqual(arr[1], 5.6)
            self.assertEqual(arr[-1], 5.8)
            self.assertEqual(arr.dtype, float)

    def test_106_subscript(self):
        for cls in self._classes:
            arr = cls([1] * 3)
            with self.assertRaises(Exception):
                _ = arr[3]
                _ = arr[-4]

    def test_107_subscript(self):
        for cls in self._classes:
            arr = cls([1.5] * 3)
            with self.assertRaises(Exception):
                _ = arr[3]
                _ = arr[-4]

    def test_108_subscript(self):
        for cls in self._classes:
            arr = cls(['hi'] * 3)
            with self.assertRaises(Exception):
                _ = arr[3]
                _ = arr[-4]

    def test_109_subscript(self):
        for cls in self._classes:
            arr = cls([1, 2, 3])
            result = arr[1:]
            self.assertEqual(result.size, 2)
            self.assertEqual(result.dtype, int)
            self.assertEqual(result[0], 2)
            self.assertEqual(result[1], 3)

    def test_110_subscript(self):
        for cls in self._classes:
            arr = cls([1, 2, 3])
            result = arr[-2:]
            self.assertEqual(result.size, 2)
            self.assertEqual(result.dtype, int)
            self.assertEqual(result[0], 2)
            self.assertEqual(result[1], 3)

    def test_111_subscript(self):
        for cls in self._classes:
            arr = cls([1, 2, 3])
            result = arr[:]
            self.assertEqual(result.size, 3)
            self.assertEqual(result.dtype, int)
            self.assertEqual(result[0], 1)
            self.assertEqual(result[1], 2)
            self.assertEqual(result[2], 3)

    def test_112_subscript(self):
        for cls in self._classes:
            arr = cls([1, 2, 3])
            result = arr[:]
            self.assertEqual(result.size, 3)
            self.assertEqual(result.dtype, int)
            self.assertEqual(result[0], 1)
            self.assertEqual(result[1], 2)
            self.assertEqual(result[2], 3)

    def test_113_subscript(self):
        for cls in self._classes:
            arr = cls([1, 2, 3])
            result = arr[::-1]
            self.assertEqual(result.size, 3)
            self.assertEqual(result.dtype, int)
            self.assertEqual(result[0], 3)
            self.assertEqual(result[1], 2)
            self.assertEqual(result[2], 1)

    def test_114_subscript(self):
        for cls in self._classes:
            arr = cls([1, 2, 3, 4, 5, 6])
            result = arr[1::2]
            self.assertEqual(result.size, 3)
            self.assertEqual(result.dtype, int)
            self.assertEqual(result[0], 2)
            self.assertEqual(result[1], 4)
            self.assertEqual(result[2], 6)

    def test_115_subscript(self):
        for cls in self._classes:
            arr = cls([1, 2, 3, 4, 5, 6])
            result = arr[::2]
            self.assertEqual(result.size, 3)
            self.assertEqual(result.dtype, int)
            self.assertEqual(result[0], 1)
            self.assertEqual(result[1], 3)
            self.assertEqual(result[2], 5)

if __name__ == '__main__':
    unittest.main()
