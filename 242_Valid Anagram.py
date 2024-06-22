from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqMap = defaultdict(int)

        for i in range(len(s)):
            freqMap[ord(s[i])] += 1
            freqMap[ord(t[i])] -= 1

        return all(value == 0 for value in freqMap.values())
