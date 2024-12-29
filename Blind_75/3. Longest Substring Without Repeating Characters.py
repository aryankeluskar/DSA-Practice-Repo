class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 1

        if len(s) <= 1:
            return len(s)

        curr_chars = set()

        while right < len(s):
            # print(set(s[left:right]), s[left:right], left, right)
            # print(curr_chars)

            if s[right] not in curr_chars:
                curr_chars.add(s[right])
                right += 1

            else:
                if (right - left) > longest:
                    longest = (right - left)

                curr_chars.remove(s[left])
                left += 1

        longest = max(longest, len(s) - left)

        return longest