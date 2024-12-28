class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        left, right = 0, 1

        while right < len(prices):

            diff = prices[right] - prices[left]

            if diff > res:
                print(left, right)
                res = diff

            
            if diff < 0:
                # most important intuition: if we find a lower buying price (ie: left pointer) then update left to match 
                left = right
            
            right += 1

            # do not put right incrementer inside if since conditions may not be met
            # also dont incrememnt left unless a lower value is found

        return res