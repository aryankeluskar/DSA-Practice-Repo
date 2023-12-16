from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lengthList = []
        for i in nums:
            lengthList.append(target - i)
        print(lengthList)
        for i in range(len(lengthList)):
            if lengthList[i] in nums and (nums.index(lengthList[i]) != i):
                return [i, nums.index(lengthList[i])]



s = Solution()
print(s.twoSum([3, 3, 4], 6))
