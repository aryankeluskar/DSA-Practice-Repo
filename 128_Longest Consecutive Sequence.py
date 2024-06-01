class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        ele = set()
        les = nums[0]
        for i in nums:
            ele.add(i)
            les = min(les, i)

        maxC = 0

        for num in ele:
            if num - 1 not in ele:
                curr = num
                count = 1

                while curr + 1 in ele:
                    curr += 1
                    count += 1

                maxC = max(maxC, count)

        return maxC
        