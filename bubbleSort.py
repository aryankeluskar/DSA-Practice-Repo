# December 7, 2023

import random

def main():
   size = int(input("what size: "))
   a = []

   for i in range(0, size):
      a.append(int(random.random()*1000+1))

   print("Original Array: "+str(a))

   bubblesort(a)


   print("Sorted Array: "+str(a))

def bubblesort(a):
   for i in range(0, len(a)):
      for j in range(0, len(a)-1):
         if(a[j] > a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]

main()