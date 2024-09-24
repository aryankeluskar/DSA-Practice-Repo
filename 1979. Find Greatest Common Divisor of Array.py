class Solution:
    def checkNum(self, nums, i):
        for j in nums:
            if not j % i == 0:
                return False

        return True

    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)

        for i in range(math.gcd(mx, mn), 0, -1):
            if self.checkNum(nums, i):
                return i
            
        return 1