   import java.util.*;

   /**
    * 49_Group Anagrams
    */
   class Solution {
      public List<List<String>> groupAnagrams(String[] strs) {
         HashMap<String, List<String>> anagrams = new HashMap<>();
         for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String newStr = new String(ca);
            if (!anagrams.containsKey(newStr)) {
               List<String> anas = new ArrayList<>();
               anas.add(s);
               anagrams.put(newStr, anas);
            } else {
               anagrams.get(newStr).add(s);
            }
         }
         return new ArrayList<>(anagrams.values());
      }
   }