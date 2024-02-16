from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # start by filling up with bricks
        # get the max, replace with ladder
        # ditribute the newly obtained bricks ahead

         bricks_needed = []
         bricks_freed = 0
         last_index = 0
         for i in range(1, len(heights)):
               diff = heights[i] - heights[i-1]
               if diff > 0:
                  bricks_needed.append(diff)
               else:
                  bricks_needed.append(0)
               last_index = i

         for i in range(ladders):
            max_val = max(bricks_needed)
            if max_val > 0:
               bricks_freed += max_val
               bricks_needed[bricks_needed.index(max_val)] = 0
            else:
               break
                  
         for i in range(last_index, len(bricks_needed)):
               diff = bricks_needed[i]
               if diff > 0:
                  if diff <= bricks_freed:
                     bricks_freed -= diff
                     # bricks_freed += diff
                  else:
                     break
               last_index = i
                   
         
         return last_index+1
                   

      #   now get the top len(ladders) elements and replace them with 0, add them to bricks_freed and itrerate through buildings heights again from wherver we last left off