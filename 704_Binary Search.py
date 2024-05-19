class Solution:
    def searchHelper(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l > r:
            return -1
        
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] > target:
            return self.searchHelper(nums, target, l, m - 1)
        if nums[m] < target:
            return self.searchHelper(nums, target, m + 1, r)

    def search(self, nums: List[int], target: int) -> int:
        return self.searchHelper(nums, target, 0, len(nums) - 1)
