#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highlight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY reels
#

def highlight(n, m, k, reels):
    # Write your code here
    canvas = [[0 for _ in range(m)] for _ in range(n)]
    for row in reels:
        for i in range(row[1], row[2] + 1):
            canvas[row[0]][i] = 1
    
    count = 0
    for i in range(n):
        for j in range(m):
            if canvas[i][j] == 0:
                count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    reels = []

    for _ in range(k):
        reels.append(list(map(int, input().rstrip().split())))

    result = highlight(n, m, k, reels)

    fptr.write(str(result) + '\n')

    fptr.close()
