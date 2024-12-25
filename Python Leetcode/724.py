class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [nums[0]]
        right_sum = [0] * len(nums)
        right_sum[0] = nums[:-1]

        for i in range(1, len(nums)):

            left_sum.append(left_sum[i-1] + nums[i])
            
            right_sum[i] = (right_sum[i - 1] + nums[len(nums)-i])

        print(left_sum)
        print(right_sum)

        return 1