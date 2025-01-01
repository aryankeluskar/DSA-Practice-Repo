class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        opening = ['(', '{', '[']
        openers = {')':"(", '}':"{", ']':"["}
        closing = [')', '}', ']']
        for i in s:
            # print(i, stack)
            if i in opening:
                stack.append(i)

            elif i in closing:
                if len(stack) == 0:
                    return False
                    
                if stack.pop() != openers[i]:
                    return False

        return len(stack) == 0