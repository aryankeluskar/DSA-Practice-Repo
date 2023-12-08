import random

def main():
   size = int(input("what size: "))
   a = []

   for i in range(0, size):
      a.append(int(random.random()*1000+1))

   print("Original Array: "+str(a))

   quicksort(a, 0, len(a)-1)

   print("Sorted Array: "+str(a))


def quicksort(a, low, high):
   if low < high:
      end = partition(a, low, high)
      quicksort(a, low, end)
      quicksort(a, end + 1, high)

def partition(a, low, high):
   mid = int((low+high)/2)
   pivot = a[mid]

   done = False
   while(not(done)):
      while(a[low] < pivot):
         low+=1
      while(a[high] > pivot):
         high-=1
      
      if (low >= high):
         done = True
      else:
         a[low], a[high] = a[high], a[low]
         low+=1
         high-=1
   
   return high

main()