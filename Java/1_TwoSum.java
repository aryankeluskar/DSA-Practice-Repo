import java.util.HashMap;

class SolutionTwo {
   public int[] twoSum(int[] nums, int target) {
      HashMap<Integer, Integer> map = new HashMap<>();
      for (int i = 0; i < nums.length; i++) {
         int complement = target - nums[i];
         if (map.containsKey(complement)) {
            return new int[] { map.get(complement), i };
         }
         map.put(nums[i], i);
      }
      return new int[] { -1, -1 }; // Return [-1, -1] if no solution found
   }

   public static void main(String[] args) {
      SolutionTwo s = new SolutionTwo();
      int[] result = s.twoSum(new int[] { 3, 3, 4 }, 6);
      System.out.println(result[0] + " " + result[1]);
   }
}