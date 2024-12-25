class Solution1624:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # use a sliding window for every char in s
        # for i from a to z, if i in s then find the longest string and store in max
        # if greater than max then modify max

        max = -1
        seen = [""]

        for cc in s:
            if cc not in seen:
                #  print("checking for " + str(cc))
                if max < (s.rfind(cc) - s.find(cc) - 1):
                    max = s.rfind(cc) - s.find(cc) - 1
                seen.append(cc)

        return max

    #   pass


s = Solution1624()
print(s.maxLengthBetweenEqualCharacters("abca"))
