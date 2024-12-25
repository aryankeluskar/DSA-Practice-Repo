// June 21, 2021

public class sorted {
   boolean isSorted(int a[]) {
      for (int i = 0; i < a.length; i++) {
         for (int j = i; j < a.length; j++) {
            if (a[i] > a[j])
               return false;
         }
      }
      return true;
   }

   boolean isSorted(String a[]) {
      for (int i = 0; i < a.length; i++) {
         for (int j = i; j < a.length; j++) {
            if (a[i].compareTo(a[j]) < 0)
               return false;
         }
      }
      return true;
   }
}