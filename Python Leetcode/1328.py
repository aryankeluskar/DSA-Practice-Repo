class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""

        p = list(palindrome)

        n = len(palindrome)

        for i in range(n):
            if not p[i] == "a":
                p[i] = "a"
                break

        # print(p)
        if p != p[::-1]:
            return "".join(p)

        p = list(palindrome)
        for i in range(n-1, -1, -1):
            if p[i] == "a":
                p[i] = "b"
                break

        return "".join(p)
