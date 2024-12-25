class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}

        if len(s) != len(t):
            return False

        for idx in range(len(s)):
            char = s[idx]
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1

            char2 = t[idx]
            if char2 in char_map:
                char_map[char2] -= 1
            else:
                char_map[char2] = -1

        for key in char_map.keys():
            if char_map[key] != 0:
                return False

        return True