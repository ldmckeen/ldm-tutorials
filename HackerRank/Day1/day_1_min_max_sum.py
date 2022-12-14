#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # sorted_arr = sorted(arr)
    # min_count = 0
    # max_count = 0
    # min_arr = sorted_arr[:4]
    # max_arr = sorted_arr[-4:]
    #
    # for i in min_arr:
    #     min_count = min_count + i
    #
    # for i in max_arr:
    #     max_count = max_count + i
    #
    # print(f"{min_count} {max_count}")

    sorted_arr = sorted(arr)
    min = sum(sorted_arr[:-1])
    max = sum(sorted_arr[1:])

    print(f"{min} {max}")


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    arr = list(map(int, input.rstrip().split()))

    miniMaxSum(arr)
