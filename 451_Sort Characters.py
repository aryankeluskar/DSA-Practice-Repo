from collections import defaultdict

class Solution:
    

    def frequencySort(self, s: str) -> str:
        freq = defaultdict()
        for c in s:
            try:
                freq[c] += 1    
            except:
                freq[c] = 1
        
        keys = list(freq.keys())
        values = list(freq.values())

        for i in range(len(values)):
            maxIndex = i
            for j in range(i, len(keys)):
                if values[j] > values[maxIndex]:
                    maxIndex = j

            values[i], values[maxIndex] = values[maxIndex], values[i]
            keys[i], keys[maxIndex] = keys[maxIndex], keys[i]
            

        final = ''
        print(keys)
        print(values)
        for i in range(len(keys)):
            final += (keys[i]*values[i])

        return final


s = Solution()
print(s.frequencySort("tree"))  