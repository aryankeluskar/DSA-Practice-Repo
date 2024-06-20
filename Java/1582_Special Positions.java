class Solution {
   public int numSpecial(int[][] mat) {
       int res=0;
       Outer:
       for(int i =0;i<mat.length;i++){
           int sIndex=-1;
           for(int j =0; j<mat[0].length;j++){
               if(mat[i][j]==1){
                   if(sIndex == -1)
                       sIndex = j;
                   else if(sIndex != -1)
                       continue Outer;
               }
           }
           if(sIndex == -1)
               continue Outer;
           if(isInSpecialCol(mat, i, sIndex))
               res++;
       }
       return res;
   }
   public boolean isInSpecialCol(int[][] mat,int i,int sIndex){
       for(int j=0;j<i;j++){
           if(mat[j][sIndex]==1)
               return false;
       }
       for(int j=i+1;j<mat.length;j++){
           if(mat[j][sIndex]==1)
               return false;
       }
       return true;
   }
}