#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'subpal' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER str_length
#  2. STRING input_str
#

def ispalindrome(s):
    return s == s[::-1]

def subpal(str_length, input_str):
    # using sliding window technique
    longest = ""
    for i in range(str_length):
        for j in range(i, str_length):
            sub = input_str[i:j+1]
            if ispalindrome(sub) and len(sub) > len(longest):
                longest = sub

    return longest

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    str_length = int(input().strip())

    input_str = input()

    result = subpal(str_length, input_str)

    fptr.write(result + '\n')

    fptr.close()
