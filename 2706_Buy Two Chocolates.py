from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        og_money = money
        count = 0
        for i in prices:
            if money >= i:
                count += 1
                money -= i
            if count >= 2:
                return money
        if count < 2:
            return og_money
        return money
