class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i in range(len(nums)):
            diff_map[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in diff_map.keys():
                if i != diff_map[nums[i]]:
                    return [i, diff_map[nums[i]]]