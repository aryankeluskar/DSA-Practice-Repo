# December 7, 2023

import random

def main():
   size = int(input("what size: "))
   a = []

   for i in range(0, size):
      a.append(int(random.random()*1000+1))

   print("Original Array: "+str(a))
   selectionSort(a)
   print("Sorted Array: "+str(a))

def selectionSort(a):
   r"""
   Sorts a list of elements in ascending order using the selection sort algorithm.

   ### Parameters:
       a (list): The list of elements to be sorted.

   ### Returns:
       None: The function modifies the input list in-place.
   """
   for i in range(0, len(a)):
      minIndex = i
      for j in range(i, len(a)):
         if(a[j] < a[minIndex]):
            minIndex = j
          
      a[i], a[minIndex] = a[minIndex], a[i]

main()