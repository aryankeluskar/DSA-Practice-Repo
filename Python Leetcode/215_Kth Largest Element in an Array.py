from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        curr_max = 0
        for i in range(1, k + 1):
            curr_max = 0
            for j in range(len(nums)):
                if nums[j] > nums[curr_max]:
                    curr_max = j

            if i < k:
                nums.pop(curr_max)

        return nums[curr_max]
