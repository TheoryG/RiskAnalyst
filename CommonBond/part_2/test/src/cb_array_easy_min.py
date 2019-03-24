"""
CBDataFrame class implementation.
"""

import unittest

from src.cb_array import CBArray

# ------------------------------------- Please do NOT use extra import statements --------------------------------------


class CBArrayEasyMin(CBArray):
    """
    A subclass of `CBArray` that's capable of returning the minimal element in the array in constant run-time. Please
    make this implementation as efficient as possible, assuming that insertion, deletion and update happens in
    relatively lower frequency, but `get_min` method is called at a much higher frequency.
    """

    def get_min(self):
        """
        Get the min element of this array. If array is empty, return None.
        Run-time complexity must be O(1), space complexity must be less than or equal to O(n).
        :return: Min element in the array.
        """
        if self.min == float('inf'):
            return None
        return self.min
        
        pass  # TODO: implementation (do not use Python `min` function, since we assume its run-time complexity is O(n))

    # TODO: you can override any method you think necessary (please make them as time efficient as possible)
