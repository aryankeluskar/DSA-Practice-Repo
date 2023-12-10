from typing import List
from collections import defaultdict


class Solution:
      def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         anagram_map = defaultdict(list)
         result = []

         for s in strs:
            #   print(''.join(sorted(s)))
            anagram_map[''.join(sorted(s))].append(s) 
            # sorting the chars in string, and then converting the char array to string 

         return anagram_map.values()
   
def main():
      sol = Solution()
      print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


if __name__ == "__main__":
    main()