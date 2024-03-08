class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        print(freq)
        out = []

        for _ in range(k):
            maxE = list(freq.keys())[0]
            for j in list(freq.keys()):
                if freq[j] > freq[maxE]:
                    maxE = j
            
            out.append(maxE)
            freq.pop(maxE)

        return out