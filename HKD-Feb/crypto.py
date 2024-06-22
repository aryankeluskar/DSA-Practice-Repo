#!/bin/python3

import os

#
# Complete the 'crypto' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER str_length
#  2. STRING input_str
#  3. STRING key
#  4. INTEGER flag
#


def crypto(str_length, input_str, key, flag):
    # Write your code here
    final_str = ""
    if flag == 0:
        for i in input_str:
            if i.isalpha():
                loc = ord(i) - 97
                print(loc)
                final_str += key[loc]
            else:
                final_str += i
    else:
        for i in input_str:
            if i.isalpha():
                final_str += chr(key.index(i) + 97)
            else:
                final_str += i

    return final_str


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    str_length = int(input().strip())

    input_str = input()

    key = input()

    flag = int(input().strip())

    result = crypto(str_length, input_str, key, flag)

    fptr.write(result + "\n")

    fptr.close()
