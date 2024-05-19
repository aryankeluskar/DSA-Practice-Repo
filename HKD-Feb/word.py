#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'wordsearch' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER grid_rows
#  2. INTEGER columns
#  3. INTEGER word_dict_count
#  4. STRING_ARRAY word_dict
#  5. 2D_CHARACTER_ARRAY grid
#

def search(grid, row, col, x, y, word):
    # check if first letter of word is at position (row, col)
    if grid[row][col] != word[0]:
        return [None, False]
    
    # length of word
    length = len(word)
    rev_word = word[::-1]
    last_index = (0,0)
    
    # check in all 8 directions
    for i in range(1, length):
        # check if position is out of grid
        if (row + i*x) < 0 or (row + i*x) >= len(grid) or (col + i*y) < 0 or (col + i*y) >= len(grid[0]):
            return [None, False]
        # check if letter at position (row + i*x, col + i*y) is same as letter at position i in word
        if grid[row + i*x][col + i*y] != word[i] and grid[row + i*x][col + i*y] != rev_word[i]:
            return [None, False]
        last_index = (row + i*x, col + i*y)

    return [last_index, True]

def wordsearch(grid_rows, columns, word_dict_count, word_dict, grid):
    # new_word_dict = []
    found_map = []

    # array of all first letters of word_dict
    first_letters = []
    for word in word_dict:
        first_letters.append(word[0])

    count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(found_map)
            
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k == 0 and l == 0:
                        continue
                    for word in word_dict:
                        result = search(grid, i, j, k, l, word)
                        if result[1]:
                            if [word, [result[0], (i,j)]] in found_map:
                                continue
                            if [word, [(i,j), result[0]]] in found_map:
                                continue
                            if [word[::-1], [(i,j), result[0]]] in found_map:
                                continue
                            if [word[::-1], [result[0], (i,j)]] in found_map:
                                continue
                            count += 1
                            found_map.append([word, [result[0], (i,j)]])
                            # print("Found", word, "at", i, j, "in direction", k, l)

    return count



# main()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    grid_rows = int(first_multiple_input[0])

    columns = int(first_multiple_input[1])

    word_dict_count = int(first_multiple_input[2])

    word_dict = input().rstrip().split()

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(lambda x: x[0], input().rstrip().split())))

    result = wordsearch(grid_rows, columns, word_dict_count, word_dict, grid)

    fptr.write(str(result) + '\n')

    fptr.close()


