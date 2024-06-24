class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend / divisor > 0:
            answer = dividend // divisor
        else:
            answer = -1 * (abs(dividend) // abs(divisor))

        if answer > pow(2, 31) - 1:
            return pow(2, 31) - 1

        if answer < -1 * pow(2, 31):
            return -1 * pow(2, 31)

        return answer
