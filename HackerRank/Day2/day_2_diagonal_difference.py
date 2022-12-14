#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    left_to_right = 0
    right_to_left = 0

    rev_arr = arr.copy()
    rev_arr.reverse()

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j == i:
                left_to_right += arr[i][j]
        for k in range(len(rev_arr[i])):
            if k == i:
                right_to_left += rev_arr[i][k]


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())

    arr = []
    arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
    # arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    # for _ in range(3):
    #     arr.append(list(map(int, input.rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
