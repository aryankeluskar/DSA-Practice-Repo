class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        oc = 0
        tc = 0
        for i in s:
            if i == "1":
                oc += 1
            else:
                tc += 1

        return "1" * (oc - 1) + "0" * tc + "1"
