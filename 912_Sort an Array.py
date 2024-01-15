# will use insertion sort cause i am reminded of your mom

from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            curr = i
            j=i-1
            while(nums[j]>nums[curr] and j>=0):
                nums[j], nums[curr] = nums[curr], nums[j]
                j-=1
                curr-=1
            print(nums)
        return nums
    
s912 = Solution()
s912.sortArray([5,2,3,1])