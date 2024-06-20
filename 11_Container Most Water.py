class Solution:
    def maxArea(self, height: List[int]) -> int:
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
                if height[l+1] >= height[r - 1]:
                    l += 1
                else:
                    r -= 1

        return ma