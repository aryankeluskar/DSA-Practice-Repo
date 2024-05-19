#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'word_jumble' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts following parameters:
#  1. STRING Word
#  2. STRING Jumble
#

def word_jumble(Word, Jumble):
    # Write your code here
    jumarr = list(Jumble)
    for i in Word:
        if i in jumarr:
            jumarr.remove(i)
        else:
            return 'N'
        
    return 'Y'
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    Word = input()

    Jumble = input()

    result = word_jumble(Word, Jumble)

    fptr.write(str(result) + '\n')

    fptr.close()
