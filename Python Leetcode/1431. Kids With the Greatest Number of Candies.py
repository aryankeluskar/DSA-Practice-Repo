class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = [False]*len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                out[i] = True

        return out