import java.util.HashMap;
import java.util.Map;

class Solution928 {

   public int lengthOfLongestSubstringTwoDistinct2(String s) {
      if (s == null || s.isEmpty()) {
         return 0;
      }

      int max = 0;

      // Store positions of the two distinct characters
      int c1pos = -1, c2pos = -1;

      for (int i = 0; i < s.length(); i++) {
         char currentChar = s.charAt(i);

         if (c1pos == -1) {
            c1pos = i;
         } else if (c2pos == -1 && currentChar != s.charAt(c1pos)) {
            c2pos = i;
         } else if (currentChar != s.charAt(c1pos) && currentChar != s.charAt(c2pos)) {
            // Update the max length
            max = Math.max(max, i - c1pos);

            // Move the starting position to the next character after the first distinct
            // character
            c1pos = Math.min(c1pos, c2pos) + 1;

            // Update positions of the two distinct characters
            c2pos = i;
         }
      }

      // Calculate the max length for the last substring
      max = Math.max(max, s.length() - c1pos);

      return max;

   }

   public static void main(String[] args) {
      Solution928 solution = new Solution928();
      System.out.println(solution.lengthOfLongestSubstringTwoDistinct2("ababacccccc"));
   }
}
