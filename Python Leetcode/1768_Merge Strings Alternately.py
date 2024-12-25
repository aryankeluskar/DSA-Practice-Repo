class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        fin = min(len(word1), len(word2))
        fin = int(fin)
        s = ""

        for i in range(fin):
            s += word1[i]
            s += word2[i]

        return s + word1[fin:] + word2[fin:]
