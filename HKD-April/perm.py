#!/bin/python3

import os

#
# Complete the 'evil_perm' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def evil_perm(n, k):
    # For an array of the first n positive integers, an evil permutation "arr" with respect to an integer k is one such that abs(arr[i] - i) = k for all i between 1 and n inclusive (assuming this array is 1-indexed). Given n and k, determine if an evil permutation exists, and if so, return the smallest one. Otherwise, return [-1].
    # Write your code here
    # if n is 1, return [1]
    if n == 1:
        return [1]
    
    # if k is 0, return [-1]
    if k == 0:
        return [-1]
    
    # if k is greater than n-1, return [-1]
    if k > n-1:
        return [-1]
    
    # if k is equal to n-1, return [n]
    if k == n-1:
        return [n]
    
    # if k is less than n-1, return [k+2, k+1, 1, k+3, k+4, ..., n, n-1, k+1]
    return [i for i in range(k+2, n+1)] + [k+1, 1] + [i for i in range(k+3, k+2)] + [n, n-1, k+1]

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    result = evil_perm(n, k)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
