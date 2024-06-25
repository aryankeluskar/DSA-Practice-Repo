class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divide two integers and handle overflow.

        Args:
            dividend (int): The dividend integer.
            divisor (int): The divisor integer.

        Returns:
            int: The result of the division, or the maximum or minimum integer value if there is overflow.
        """
        if dividend / divisor > 0:
            answer = dividend // divisor
        else:
            answer = -1 * (abs(dividend) // abs(divisor))

        if answer > pow(2, 31) - 1:
            return pow(2, 31) - 1

        if answer < -1 * pow(2, 31):
            return -1 * pow(2, 31)

        return answer
