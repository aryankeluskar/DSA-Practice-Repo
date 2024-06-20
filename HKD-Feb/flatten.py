#!/bin/python3

import os

#
# Complete the 'flatten_heights' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def flatten_heights(arr):
    total = sum(arr)
    attain = total // len(arr)
    diff = []
    
    for i in arr:
        diff.append(abs(i - attain))

    return sum(diff)





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = flatten_heights(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
