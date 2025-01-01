class Solution:
    def getCounter(self, s: str) -> dict:
        counter = {}
        for char in s:
            counter[char] = 1 + counter.get(char, 0)
        return counter

    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        counter_t = self.getCounter(t)
        counter_s = {}
        need = len(counter_t) 
        have = 0

        left, right = 0, 0
        min_len = float("inf")
        min_window = ""

        while right < len(s):
            char = s[right]
            counter_s[char] = 1 + counter_s.get(char, 0)

            if char in counter_t and counter_s[char] == counter_t[char]:
                have += 1

            while left <= right and have == need:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window = s[left:right + 1]

                char = s[left]
                counter_s[char] -= 1
                if char in counter_t and counter_s[char] < counter_t[char]:
                    have -= 1
                left += 1

            right += 1

        return min_window
