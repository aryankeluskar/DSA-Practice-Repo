class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_product = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            right_product[i] = nums[i + 1] * right_product[i + 1]

        left_product = [1] * len(nums)
        for i in range(1, len(nums)):
            left_product[i] *= nums[i - 1] * left_product[i - 1]

        for i in range(len(nums)):
            right_product[i] *= left_product[i]

        return right_product


        