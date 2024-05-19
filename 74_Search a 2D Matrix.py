
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowId = self.colSearchHelper(matrix, target=target, u=0, d=len(matrix))
        if rowId == -1:
            return False
        if self.rowSearchHelper(matrix[rowId], target, 0, len(matrix[rowId]) - 1) == -1:
            return False
        return True

    def colSearchHelper(self, nums: List[int], target: int, u: int, d: int) -> int:
        if u > d or len(nums)==0:
            return -1

        if len(nums)==1:
            return 0

        m = (u + d) // 2
        print(nums, m)
        try:
            if nums[m][0] <= target and nums[m][len(nums[0])-1] >= target:
                return m
            if nums[m][0] < target and nums[m][len(nums[0])-1] < target:
                return self.colSearchHelper(nums, target, m+1, d)
            if nums[m][0] > target and nums[m][len(nums[0])-1] > target:
                return self.colSearchHelper(nums, target, u, m-1)
        except:
            return -1
        

    def rowSearchHelper(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l > r:
            return -1
        
        if len(nums)==1:
            if nums[0] == target:
                return 0
            else:
                return -1

        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] > target:
            return self.rowSearchHelper(nums, target, l, m - 1)
        if nums[m] < target:
            return self.rowSearchHelper(nums, target, m + 1, r)
        
s = Solution()
print(s.searchMatrix([[1], [3]], 4))