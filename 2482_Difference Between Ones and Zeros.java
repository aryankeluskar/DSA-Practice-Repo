class Solution {
   public int[][] onesMinusZeros(int[][] grid) {
      int[][] res = new int[grid.length][grid[0].length];
      int[] rowCounts = new int[grid.length];
      int[] colCounts = new int[grid[0].length];
      
      // Calculate row counts
      for (int i = 0; i < grid.length; i++) {
         rowCounts[i] = onesInRow(i, grid);
      }
      
      // Calculate column counts
      for (int j = 0; j < grid[0].length; j++) {
         colCounts[j] = onesInCol(j, grid);
      }
      
      // Calculate ones minus zeros
      for (int i = 0; i < grid.length; i++) {
         for (int j = 0; j < grid[0].length; j++) {
            res[i][j] = rowCounts[i] + colCounts[j] - (grid[0].length - rowCounts[i]) - (grid.length - colCounts[j]);
         }
      }
      
      return res;
   }

   public int onesInRow(int row, int[][] grid) {
      int count = 0;
      for (int i = 0; i < grid[row].length; i++) {
         if (grid[row][i] == 1) {
            count++;
         }
      }
      return count;
   }

   public int onesInCol(int col, int[][] grid) {
      int count = 0;
      for (int i = 0; i < grid.length; i++) {
         if (grid[i][col] == 1) {
            count++;
         }
      }
      return count;
   }
}