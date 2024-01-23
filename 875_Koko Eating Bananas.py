from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1
        maxK = max(piles)
        
        res = maxK

        while minK <= maxK:
            mid = (minK+maxK)//2
            hours =0
            for i in piles:
                hours += math.ceil(i/mid)

            if hours <= h:
                res = min(res, mid)
                maxK = mid -1
            else:
                minK = mid+1

        return res

            
        return self.searchHelper(1, maxK, h, piles)


    def searchHelper(self, low: int, high: int, h: int, piles: List[int]) -> int:
        mid = (low+high)//2
        hours = self.hoursTaken(mid, piles)
        if hours <= h:
            for i in range(mid, low-1, -1):
                if self.hoursTaken(i, piles) > h:
                    return i+1
                
        if hours > h:
            return self.searchHelper(mid+1, high, h, piles)


    def hoursTaken(self, k: int, piles: List[int]) -> int:
        sumK = 0
        for i in piles:
            if not (i % k==0):
                sumK+=1
            sumK += (i//k)
        
        return sumK
    

s = Solution()
print(f"final is {s.minEatingSpeed([312884470], 312884469)}")