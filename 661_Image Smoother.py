import math
from typing import List

class Solution:
   def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
      rows = len(img)
      cols = len(img[0])
      result = [[0] * cols for _ in range(rows)]  

      for i in range(rows):
         for j in range(cols):
            # result at i,j is the sum of all neighbors
            total = img[i][j]
            count = 1

            if i > 0:
               total += img[i-1][j]
               count += 1
            if j > 0:
               total += img[i][j-1]
               count += 1
            if i < rows-1:
               total += img[i+1][j]
               count += 1
            if j < cols-1:
               total += img[i][j+1]
               count += 1
            if i > 0 and j > 0:
               total += img[i-1][j-1]
               count += 1
            if i > 0 and j < cols-1:
               total += img[i-1][j+1]
               count += 1
            if i < rows-1 and j > 0:
               total += img[i+1][j-1]
               count += 1
            if i < rows-1 and j < cols-1:
               total += img[i+1][j+1]
               count += 1

            result[i][j] = math.floor(total / count)
      return result

