#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    arr_len = len(arr)
    zero_count = 0
    pos_count = 0
    neg_count = 0
    for n in arr:
        if n == 0:
            zero_count += 1
        elif n < 0:
            neg_count += 1
        else:
            pos_count += 1

    print("{:.6f}".format(pos_count/arr_len))
    print("{:.6f}".format(neg_count/arr_len))
    print("{:.6f}".format(zero_count/arr_len))


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])

    arr = list(map(int, input.rstrip().split()))

    plusMinus(arr)
