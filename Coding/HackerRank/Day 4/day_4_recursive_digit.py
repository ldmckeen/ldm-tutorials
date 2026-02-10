#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

"""
def sup_digits(x,k):
    a = digsum(x)
    return sup_digit(str(int(a)*k))

def sup_digit(x):
    if len(x) <= 1:
        return x
    else:
        return sup_digit( digsum(x) )

def digsum(x):
    return str(sum((int(i) for i in list(x))))
"""

"""
def digits_sum(n):
    s = 0
    while n > 9:
        s += n % 10
        n //= 10
    s += n
    return s


def super_digit(n):
    d = digits_sum(n)
    if d < 10:
        return d
    return super_digit(d)


def super_digit_iter(n):
    d = digits_sum(n)
    while d > 9:
        d = digits_sum(d)
    return d
"""

def superDigit(n, k):
    # Write your code here
    # if len(n) == 1:
    #     return n
    # str_n = ""
    # for i in range(k):
    #     str_n += str(n)
    # s_sum = 0
    # for i in str_n:
    #     s_sum += int(i)
    # new_str_n = str(s_sum)
    # return superDigit(new_str_n, 1)

    # return super_digit_iter(digits_sum(int(n)) * k)

    return 1 + (k * sum(int(x) for x in n) - 1) % 9
    # https://www.xarg.org/puzzle/hackerrank/recursive-digit-sum/


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input.rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
