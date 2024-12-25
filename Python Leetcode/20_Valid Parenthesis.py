class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {"]": "[", "}": "{", ")": "("}
        stack = []
        for c in s:
            # if c in bracketMap.keys():
            #     print(bracketMap[c])
            # print(c)
            if c in bracketMap.keys():
                if stack and bracketMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            if c not in bracketMap.keys():
                stack.append(c)
            #  print(stack)

        if stack:
            return False
        return True


s = Solution()
print(s.isValid("({{{{}}}))"))
