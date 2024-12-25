from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[-1] * sorted_nums[-2] - sorted_nums[0] * sorted_nums[1]


s = Solution()
print(s.maxProductDifference([1, 6, 7, 5, 2, 4, 10, 6, 4]))
