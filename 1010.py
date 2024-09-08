from math import comb

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = {} 
        for x in range(60):
            freq[x] = 0

        for i in time:
            i = i % 60
            if i in freq.keys():
                freq[i] += 1

            else:
                freq[i] = 1

        out = 0
        if 0 in freq.keys():
            out += comb(freq[0], 2)
        
        if 30 in freq.keys():
            out += comb(freq[30], 2)

        for i in range(1, 30):
            out += freq[i] * freq[60 - i]

        return out