from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ind = []
        days = [0]*len(temperatures)
        # print(days)
        for i in range(len(temperatures)):
            while ind and temperatures[ind[-1]] < temperatures[i]:
                doneInd = ind.pop()
                days[doneInd] = i - doneInd
            ind.append(i)
                
        return days


s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))