class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left, right = 0, len(heights)-1
        # res = (right - left) * min(heights[left], heights[right])

        while left < right:
            current = (right - left) * min(heights[left], heights[right])
            # print(left, right, current)
            if current > res:
                res = current

            if heights[left] <= heights[right]:
                left += 1

            else:
                right -= 1

        return res