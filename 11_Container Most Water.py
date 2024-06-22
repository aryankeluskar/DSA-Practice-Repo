from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        r"""
        Calculates the maximum area between two vertical lines in a container.

        Args:
            height (List[int]): A list of integers representing the heights of the lines.

        Returns:
            int: The maximum area between two vertical lines.

        Example:
            >>> s = Solution()
            >>> s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
            49
        """
        l, r = 0, len(height) - 1

        ma = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if area > ma:
                ma = area

            if height[l] > height[r]:
                r -= 1

            elif height[l] < height[r]:
                l += 1

            elif height[l] == height[r]:
                if height[l + 1] >= height[r - 1]:
                    l += 1
                else:
                    r -= 1

        return ma
