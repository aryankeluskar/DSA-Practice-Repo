#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cool_dev' function below.
#
# The function is expected to return a FLOAT.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cool_dev(arr):
    # Write your code here
    if len(arr) == 1:
        return "{out:.3f}".format(out=0.0)
    mean = sum(arr)/len(arr)
    cube_sum = 0
    for i in arr:
        cube_sum += abs((i-mean)*(i-mean)*(i-mean))

    cube_sum /= len(arr)
    return pow(cube_sum, 1/3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cool_dev(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
