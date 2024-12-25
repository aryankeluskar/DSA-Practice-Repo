#!/bin/python3

import os

#
# Complete the 'tic_tac' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts 2D_CHARACTER_ARRAY grid as parameter.
#


def tic_tac(grid):
    for row in grid:
        if row.count("X") == 2 and row.count("S") == 1:
            return "X"
        if row.count("O") == 2 and row.count("S") == 1:
            return "O"

    for i in range(3):
        col = [grid[j][i] for j in range(3)]
        if col.count("X") == 2 and col.count("S") == 1:
            return "X"
        if col.count("O") == 2 and col.count("S") == 1:
            return "O"

    diag1 = [grid[i][i] for i in range(3)]
    if diag1.count("X") == 2 and diag1.count("S") == 1:
        return "X"
    if diag1.count("O") == 2 and diag1.count("S") == 1:
        return "O"

    diag2 = [grid[i][2 - i] for i in range(3)]
    if diag2.count("X") == 2 and diag2.count("S") == 1:
        return "X"
    if diag2.count("O") == 2 and diag2.count("S") == 1:
        return "O"

    if any("S" in row for row in grid):
        return "D"

    return "N"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    grid = []

    for _ in range(3):
        grid.append(list(map(lambda x: x[0], input().rstrip().split())))

    result = tic_tac(grid)

    fptr.write(str(result) + "\n")

    fptr.close()
