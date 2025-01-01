from typing import List

class Solution:
    def findMinIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if nums[0] < nums[-1]:
            return 0

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return l 

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        minIndex = self.findMinIndex(nums)

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            realMid = (m + minIndex) % len(nums)

            if nums[realMid] == target:
                return realMid
            elif nums[realMid] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
