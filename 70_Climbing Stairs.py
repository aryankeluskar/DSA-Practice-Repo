# lmfao so i need to use decision trees, have fun aryan. 
# and also DP 
class Solution:
    def climbStairs(self, n: int) -> int:
        sum = 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
            sum = a+b
        return sum