class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for i in s:
            if i.isalnum():
                newS += i.lower()

        # print(newS)
        return newS == newS[::-1]
