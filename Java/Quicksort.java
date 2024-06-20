// December 2, 2023

import java.util.Random;
public class Quicksort {

   public static int partition(int[] arr, int lowIndex, int highIndex) {
      int midPoint = (lowIndex + highIndex) / 2;
      int pivot = arr[midPoint];
      // System.out.println("pivot: " + pivot);

      boolean done = false;

      while (!done) {
         while (arr[lowIndex] < pivot)
            lowIndex++;
         while (arr[highIndex] > pivot)
            highIndex--;
         if (lowIndex >= highIndex) {
            done = true;
         } else {
            int temp = arr[lowIndex];
            arr[lowIndex] = arr[highIndex];
            arr[highIndex] = temp;

            lowIndex++;
            highIndex--;
         }
      }
      return highIndex;
   }
   
   public static void quicksortHelper(int[] arr, int lowIndex, int highIndex) {
      if (lowIndex >= highIndex) {
         return;
      }
      int lowEndIndex = partition(arr, lowIndex, highIndex);
      quicksortHelper(arr, lowIndex, lowEndIndex);
      quicksortHelper(arr, lowEndIndex + 1, highIndex);

   }

   // Method to generate a random array
   public static int[] generateRandomArray(int size) {
      int[] array = new int[size];
      Random random = new Random();

      for (int i = 0; i < size; i++) {
         array[i] = random.nextInt(1000000); // Change the range of random numbers as per your requirement
      }

      return array;
   }

   public static void main(String args[]){
      int[] arr = generateRandomArray(10);
      System.out.println("Unsorted array: ");
      for (int i = 0; i < arr.length; i++) {
         System.out.print(arr[i]+ " ");
      }
      quicksortHelper(arr, 0, arr.length - 1);
      System.out.println("\nSorted array: ");
      for (int i = 0; i < arr.length; i++) {
         System.out.print(arr[i]+ " ");
      }
      System.out.println();
   }

}