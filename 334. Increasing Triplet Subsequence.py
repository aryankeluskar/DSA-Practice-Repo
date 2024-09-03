class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = float('inf')
        b = float('inf')

        for i in nums:
            if i <= a:
                a = i   
            elif i <= b:
                b = i
            
            if i > a and i > b:
                return True

        return False
