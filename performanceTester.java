// December 1, 2023

import java.text.DecimalFormat;
import java.util.Random;

/**
 * performanceTester
 * testing out best, worst and average case scenarios for my quicksort, GitHub Copilot's quicksort, bubblesort, selection sort and bogosort 
 */

public class performanceTester {
   public static void main(String[] args) {
      // int[] arr = { 5, 4, 3, 2, 1 };
      // System.out.println(partition(arr, 0, 4));
      // for (int i = 0; i < arr.length; i++) {
      //    System.out.print(arr[i] + " ");
      // }
      testPerfomance();
   }

   public static void testPerfomance() {
      // print details for this system which can be used to understand the performance
      // levels
      System.out.println("Number of processors: " + Runtime.getRuntime().availableProcessors());
      System.out.println("Total memory: " + Runtime.getRuntime().totalMemory());
      System.out.println("Max memory: " + Runtime.getRuntime().maxMemory());
      System.out.println("Free memory: " + Runtime.getRuntime().freeMemory());

      int iterations = 100000, sizeArray = 5;
      long totalTime = 0;
      double bestCase = 0.0, worstCase = 0.0;

      for (int i = 0; i < iterations; i++) {
         int[] array = generateRandomArray(sizeArray); // Change the size of the array as per your requirement

         long startTime = System.nanoTime();

         int lowIndex = 0, highIndex = array.length - 1;
         quicksortHelper(array, lowIndex, highIndex);

         long endTime = System.nanoTime();
         double elapsedTime = endTime - startTime;
         totalTime += elapsedTime;
         if (i == 0) {
            bestCase = elapsedTime;
            worstCase = elapsedTime;
         }
         if (elapsedTime < bestCase) {
            bestCase = elapsedTime;
         }
         if (elapsedTime > worstCase) {
            worstCase = elapsedTime;
         }
      }

      long averageTime = totalTime / iterations;

      DecimalFormat decimalFormat = new DecimalFormat("#.########");
      String formattedBestCase = decimalFormat.format(bestCase);
      String formattedWorstCase = decimalFormat.format(worstCase);
      String formattedAverageTime = decimalFormat.format(averageTime);

      System.out.println("Number of iterations: " + iterations);

      System.out.println("\nMy Quicksort:");
      System.out.println("Best case time: " + formattedBestCase + " nanoseconds");
      System.out.println("Worst case time: " + formattedWorstCase + " nanoseconds");
      System.out.println("Average time to run: " + formattedAverageTime + " nanoseconds");

      totalTime = 0;
      for (int i = 0; i < iterations; i++) {
         int[] array = generateRandomArray(sizeArray); // Change the size of the array as per your requirement
         long startTime = System.nanoTime();

         coQuickSort(array);

         long endTime = System.nanoTime();
         double elapsedTime = endTime - startTime;
         totalTime += elapsedTime;
         if (i == 0) {
            bestCase = elapsedTime;
            worstCase = elapsedTime;
         }
         if (elapsedTime < bestCase) {
            bestCase = elapsedTime;
         }
         if (elapsedTime > worstCase) {
            worstCase = elapsedTime;
         }
      }

      averageTime = totalTime / iterations;

      decimalFormat = new DecimalFormat("#.########");
      formattedBestCase = decimalFormat.format(bestCase);
      formattedWorstCase = decimalFormat.format(worstCase);
      formattedAverageTime = decimalFormat.format(averageTime);

      // System.out.println("Number of iterations: " + iterations);

      System.out.println("\nCopilot's Quicksort:");
      System.out.println("Best case time: " + formattedBestCase + " nanoseconds");
      System.out.println("Worst case time: " + formattedWorstCase + " nanoseconds");
      System.out.println("Average time to run: " + formattedAverageTime + " nanoseconds");

      totalTime = 0;
      for (int i = 0; i < iterations; i++) {
         int[] array = generateRandomArray(sizeArray); // Change the size of the array as per your requirement
         long startTime = System.nanoTime();

         bubbleSort(array);

         long endTime = System.nanoTime();
         double elapsedTime = endTime - startTime;
         totalTime += elapsedTime;
         if (i == 0) {
            bestCase = elapsedTime;
            worstCase = elapsedTime;
         }
         if (elapsedTime < bestCase) {
            bestCase = elapsedTime;
         }
         if (elapsedTime > worstCase) {
            worstCase = elapsedTime;
         }
      }

      averageTime = totalTime / iterations;

      decimalFormat = new DecimalFormat("#.########");
      formattedBestCase = decimalFormat.format(bestCase);
      formattedWorstCase = decimalFormat.format(worstCase);
      formattedAverageTime = decimalFormat.format(averageTime);

      // System.out.println("Number of iterations: " + iterations);

      System.out.println("\nBubblesort:");
      System.out.println("Best case time: " + formattedBestCase + " nanoseconds");
      System.out.println("Worst case time: " + formattedWorstCase + " nanoseconds");
      System.out.println("Average time to run: " + formattedAverageTime + " nanoseconds");

      totalTime = 0;
      for (int i = 0; i < iterations; i++) {
         int[] array = generateRandomArray(sizeArray); // Change the size of the array as per your requirement

         long startTime = System.nanoTime();

         selectionSort(array);

         long endTime = System.nanoTime();
         double elapsedTime = endTime - startTime;
         totalTime += elapsedTime;
         if (i == 0) {
            bestCase = elapsedTime;
            worstCase = elapsedTime;
         }
         if (elapsedTime < bestCase) {
            bestCase = elapsedTime;
         }
         if (elapsedTime > worstCase) {
            worstCase = elapsedTime;
         }
      }

      averageTime = totalTime / iterations;

      decimalFormat = new DecimalFormat("#.########");
      formattedBestCase = decimalFormat.format(bestCase);
      formattedWorstCase = decimalFormat.format(worstCase);
      formattedAverageTime = decimalFormat.format(averageTime);

      // System.out.println("Number of iterations: " + iterations);

      System.out.println("\nSelection:");
      System.out.println("Best case time: " + formattedBestCase + " nanoseconds");
      System.out.println("Worst case time: " + formattedWorstCase + " nanoseconds");
      System.out.println("Average time to run: " + formattedAverageTime + " nanoseconds");

      totalTime = 0;
      for (int i = 0; i < iterations; i++) {
         int[] array = generateRandomArray(sizeArray); // Change the size of the array as per your requirement

         long startTime = System.nanoTime();

         bogoSort(array);
         long endTime = System.nanoTime();
         double elapsedTime = endTime - startTime;
         totalTime += elapsedTime;
         if (i == 0) {
            bestCase = elapsedTime;
            worstCase = elapsedTime;
         }
         if (elapsedTime < bestCase) {
            bestCase = elapsedTime;
         }
         if (elapsedTime > worstCase) {
            worstCase = elapsedTime;
         }
      }

      averageTime = totalTime / iterations;

      decimalFormat = new DecimalFormat("#.########");
      formattedBestCase = decimalFormat.format(bestCase);
      formattedWorstCase = decimalFormat.format(worstCase);
      formattedAverageTime = decimalFormat.format(averageTime);

      // System.out.println("Number of iterations: " + iterations);

      System.out.println("\nBogosort:");
      System.out.println("Best case time: " + formattedBestCase + " nanoseconds");
      System.out.println("Worst case time: " + formattedWorstCase + " nanoseconds");
      System.out.println("Average time to run: " + formattedAverageTime + " nanoseconds");

   }

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

   // method for bubble sort
   public static void bubbleSort(int[] arr) {
      // System.out.println("Bubble sort");
      int n = arr.length;
      for (int i = 0; i < n - 1; i++)
         for (int j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1]) {
               // swap temp and arr[i]
               int temp = arr[j];
               arr[j] = arr[j + 1];
               arr[j + 1] = temp;
            }
   }

   // method for selection sort
   public static void selectionSort(int[] arr) {
      // System.out.println("Selection sort");
      int n = arr.length;

      // One by one move boundary of unsorted subarray
      for (int i = 0; i < n - 1; i++) {
         // Find the minimum element in unsorted array
         int min_idx = i;
         for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx])
               min_idx = j;

         // Swap the found minimum element with the first
         // element
         int temp = arr[min_idx];
         arr[min_idx] = arr[i];
         arr[i] = temp;
      }
   }

   // method named coQuickSort to perform quicksort
   public static void coQuickSort(int[] arr) {
      // System.out.println("Quick sort");
      int n = arr.length;
      coQuickSortHelper(arr, 0, n - 1);
   }

   // coQuickSortHelper here
   public static void coQuickSortHelper(int[] arr, int lowIndex, int highIndex) {
      if (lowIndex >= highIndex) {
         return;
      }
      int lowEndIndex = coPartition(arr, lowIndex, highIndex);
      coQuickSortHelper(arr, lowIndex, lowEndIndex);
      coQuickSortHelper(arr, lowEndIndex + 1, highIndex);

   }

   // coPartition here
   public static int coPartition(int[] arr, int lowIndex, int highIndex) {
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

   // method for bogosort
   public static void bogoSort(int[] arr) {
      // System.out.println("Bogo sort");
      while (isSorted(arr) == false)
         shuffle(arr);
   }

   public static boolean isSorted(int[] arr) {
      for (int i = 0; i < arr.length - 1; i++) {
         if (arr[i] > arr[i + 1]) {
            return false;
         }
      }
      return true;
   }

   public static void shuffle(int[] arr) {
      Random random = new Random();
      for (int i = 0; i < arr.length; i++) {
         int randomIndexToSwap = random.nextInt(arr.length);
         int temp = arr[randomIndexToSwap];
         arr[randomIndexToSwap] = arr[i];
         arr[i] = temp;
      }
   }
}