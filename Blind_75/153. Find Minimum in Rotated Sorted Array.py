class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            # print(nums[m])
            if nums[m] < nums[m-1]:
                return nums[m]
            
            if nums[m] < nums[r]:
                r = m - 1
            
            else:
                l = m + 1