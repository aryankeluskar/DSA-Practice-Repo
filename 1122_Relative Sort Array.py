class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        rem = []
        for i in arr2:
            freq[i] = 0
        for i in arr1:
            if i in freq:
                freq[i] += 1
            else:
                rem.append(i)

        fin = []
        for i in freq:
            fin += [i] * freq[i]

        fin += sorted(rem)

        return fin
