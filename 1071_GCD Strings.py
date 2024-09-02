class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(len(str1) > len(str2)):
            str1, str2 = str2, str1

        # so we know that str2 is defintely the longer one
        base = str1
        if(len(str2) % len(str1) == 0 and base * (len(str2) // len(str1)) == str2 ):
            return base
            
        for i in range(len(base), 1, -1):
            base = str1[:i]
            if(base * (len(str2) // len(base)) == str2 and base * (len(str1) // len(base)) == str1 ):
                return base

        return ""