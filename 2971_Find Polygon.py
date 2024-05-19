from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        for i in nums:
            sum_arr = 0
            longest = nums[0]
            for j in nums:
                sum_arr+=j
                if longest < j:
                    longest = j
            sum_arr -= longest
            if sum_arr < longest:
                return sum_arr
            else:
                nums.remove(longest)
        return -1
    

# NO WAY THIS BEAT 98% in Python3 on Leetcode woah.