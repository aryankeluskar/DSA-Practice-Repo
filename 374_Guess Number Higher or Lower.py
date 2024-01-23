# Janurary 22, 2024

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.guessNumberHelper(1, n)

    def guessNumberHelper(self, low: int, high: int) -> int:
        mid = (low+high)//2
        if guess(mid) == 0:
            return mid
        if guess(mid) == 1:
            return self.guessNumberHelper(mid+1, high)
        if guess(mid) == -1:
            return self.guessNumberHelper(low, mid-1)