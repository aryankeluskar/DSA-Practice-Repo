from collections import defaultdict
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq_map = defaultdict(int)
        for i in arr:
            freq_map[i] += 1

        for key, value in freq_map.items():
            if value > (len(arr) / 4.0):
                return key

        return -1  # If no key has a value greater than as
