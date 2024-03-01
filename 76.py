class Solution:
    def check(self, s: str, t: str) -> bool:
        if not s:
            return False
        if len(t) > len(s):
            return False
        count = {}
        curr = {}
        

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        if len(s) == len(t) and t in s:
            return t

        res = ""
        left = 0
        right = 0
        while right < len(s):
            if self.check(s[left:right+1], t):
                print(s[left:right+1])
                if not res or right - left + 1 < len(res):
                    res = s[left:right+1]
                left += 1
            else:
                right += 1

        return res
    
print("a" in "")
s = Solution()
s.minWindow("bbaa","aba")