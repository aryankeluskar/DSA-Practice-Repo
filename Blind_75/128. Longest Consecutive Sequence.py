class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        len_table = {}
        res_length = 0

        for i in range(len(nums)):
            if (nums[i] - 1 in lookup):
                continue

            start = nums[i]
            if start in len_table:
                current_length = len_table[start]
            
            else:
                current_length = 0
                while start in lookup:
                    start += 1
                    current_length += 1

                len_table[nums[i]] = current_length

            res_length = max(current_length, res_length)

        return res_length