class Solution:
    def processString(self, s: str) -> str:
        res = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                res += i

        return res.lower()

    def isPalindrome(self, s: str) -> bool:
        s = self.processString(s)

        # left = 0

        for left in range(0, len(s)//2):
            # print(s[left] , s[len(s) - left - 1])
            if not (s[left] == s[len(s) - left - 1]):
                return False

        return True