class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, right = 0, 0
        count = {}

        res = 0

        while right < len(s):
            if s[right] in count:
                count[s[right]] += 1

            else:
                count[s[right]] = 1

            if (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res