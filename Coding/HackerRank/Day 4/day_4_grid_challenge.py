#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    sorted_grid = []
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))

    is_sorted = "YES"

    # for c in grid[0]:
    #     c_index = 0
    #     tmp_s = ""
    #     while c_index < (len(grid[0]) - 1):
    #         tmp_s += (grid[c_index])[grid[0].index(c)]
    #         c_index += 1
    #     if list(tmp_s) != sorted(tmp_s):
    #         is_sorted = "NO"
    #         break

    for i in range(len(grid) - 1):
        for j in range(len(grid[0])):
            if grid[i][j] > grid[i + 1][j]:
                is_sorted = "NO"
                break

    return is_sorted


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # t = int(input.strip())

    # for t_itr in range(t):
    #     n = int(input().strip())
    #
    #     grid = []
    #
    #     for _ in range(n):
    #         grid_item = input()
    #         grid.append(grid_item)
    #
    #     result = gridChallenge(grid)
    t = 1
    n = 5
    grid = [
        'ebacd',
        'fghij',
        'olmkn',
        'trpqs',
        'xywuv'
    ]
    # result = gridChallenge(grid)
    # print(result)

    grid = [
        "abc",
        "lmp",
        "qrt"
    ]
    # result = gridChallenge(grid)
    # print(result)

    grid = [
        "mpxz",
        "abcd",
        "wlmf"
    ]
    # result = gridChallenge(grid)
    # print(result)

    grid = [
        "abc",
        "hjk",
        "mpq",
        "rtv"
    ]

    # result = gridChallenge(grid)
    # print(result)

    grid = [
        "eibjbwsp",
        "ptfxehaq",
        "jxipvfga",
        "rkefiyub",
        "kalwfhfj",
        "lktajiaq",
        "srdgoros",
        "nflvjznh"
    ]
    # result = gridChallenge(grid)
    # print(result)

    grid = [
        "zzzzzzzzeqzzzzzzzzezzzzz",
        "zzzzuzzuzzgzzzzzzzzzzzzz",
        "zzzzzzzzzuzzzzzzzzzjzzuz",
        "zzzzuzzzjzzzzzzzzzzzzuzz",
        "vzzzvzzzzzzzzzzzzozzzzzz",
        "zzzzzzzzzzzzzxzzzxzzxzzz",
        "zzzzzzzzxzzzzzzzzxxzzzzz",
        "zzzxzzzzzxzzzzzzzzzzzzzx",
        "xxzzzzzzzzzzzzzzzzzzzzzx",
        "zzzxzzxzzzzzzzzzzzzzzxzz",
        "zzxxxzzzzzzzzzzzzzzzzzzz",
        "zzxzxzzzzzzzzzzzzzzzzxzz",
        "zzzzzzzzxzzzzzzzzzzzxzxz",
        "zzzzzzzzzzzzxzzzzzzzzzzz",
        "zzzzzzzzzzzxzzzzzzzzzzzz",
        "zzzzzzxzzzzzzzzzzzzzzzzz",
        "zzzzzzzzzzzzzzxzzzzzzzzz",
        "zzzzzzzzzzzzzzzzzzzzxzzz",
        "zzzzzzzzzzzzzzzzzzzzzzzx",
        "zzzzzzzzzzzzzzzzxzzzzzzz",
        "zzzzzzzzzzzzzzzzzzzxzzzz",
        "zzzzzzzzxzzzzzzzzzzzzzzz",
        "zzzzzzzzzzzzzzzzzzzzzxzz",
        "xzzzzzzzzzzzzzzzzzzzzzzz"
    ]

    result = gridChallenge(grid)
    print(result)



    #     fptr.write(result + '\n')
    #
    # fptr.close()
