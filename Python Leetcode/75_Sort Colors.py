class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        oc = 0
        tc = 0
        zc = 0
        for i in nums:
            if i == 0:
                zc += 1
            elif i == 1:
                oc += 1
            elif i == 2:
                tc += 1

        count = 0
        while zc > 0:
            nums[count] = 0
            zc -= 1

        while oc > 0:
            nums[count] = 1
            oc -= 1

        while tc > 0:
            nums[count] = 2
            tc -= 1

        print(nums)
