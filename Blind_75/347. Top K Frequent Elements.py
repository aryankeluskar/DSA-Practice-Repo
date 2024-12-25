class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        freq = sorted(freq.items(), key=lambda item: item[1], reverse = True)
        # print(freq)
        freq = dict(freq)

        return list(freq.keys())[:k]
    

# alternate way for O(n)

# use a list where indices are frequencies and values of the array are usbarrays
# in those subarrays, store elements that have the frequency of the array index
# then traverse the list backwards till you find k elements and return.