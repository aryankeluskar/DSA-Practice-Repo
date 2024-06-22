class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        s = s.lower()
        charMap = [{"char": s[0], "count": 1}]
        # so i want a charmap to store 3 things: char, count, and index of the the group of chars in string
        for i in range(1, len(s)):
            if s[i] == charMap[-1]["char"]:
                charMap[-1]["count"] += 1
            else:
                charMap.append({"char": s[i], "count": 1})

        print(charMap)

        while k > 0:
            # finding group with smallest count and removing them. then going for those like 10 and 100, then decrementing them to 9 or 99.
            for i in range(len(charMap) - 1, -1, -1):
                if charMap[i]["count"] == 1 and k > 0:
                    charMap[i]["count"] = 0
                    k -= 1

            # if there are no more groups with count 1, then we can just decrease 10 and 100 to 9 and 99
            for i in range(len(charMap) - 1, -1, -1):
                if charMap[i]["count"] == 10 or charMap[i]["count"] == 100:
                    charMap[i]["count"] -= 1
                    k -= 1

            # now go for decreasing others which have count <= k if k > 0
            for i in range(len(charMap) - 1, -1, -1):
                if charMap[i]["count"] <= k:
                    k -= charMap[i]["count"]
                    charMap[i]["count"] = 0
                else:
                    charMap[i]["count"] -= k
                    k = 0

        # remove all groups with count 0
        charMap = [group for group in charMap if group["count"] > 0]

        result = 0
        print(charMap)
        for i in charMap:
            value = i["count"]
            result += 1 + len(str(value))
            if value == 1:
                result -= 1
        return result


s = Solution()
print(s.getLengthOfOptimalCompression("bababbaba", 1))
# babab2ab
