#!/bin/python3

import os

#
# Complete the 'longest_subarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY nums
#


def longest_subarray(n, k, nums):
    left = 0
    right = 0
    max_len = 0
    curr_sum

    while right < n:
        if nums[right] == 0:
            k -= 1

        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1

        right += 1

    return right - left - 1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    nums = list(map(int, input().rstrip().split()))

    result = longest_subarray(n, k, nums)

    fptr.write(str(result) + "\n")

    fptr.close()
