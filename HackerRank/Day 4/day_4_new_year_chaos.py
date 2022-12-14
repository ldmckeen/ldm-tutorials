#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    # Write your code here
    ride_queue = q.copy()
    ride_queue.sort()
    current_i = len(q) - 1
    b_count = 0
    total_b_count = 0
    print("New Year Queue")
    print(q)
    print("==============\n\n")

    while current_i > 0:
        print(ride_queue)
        print(f"Current Index: {current_i}")
        print(f"B-Count: {b_count}")
        print(f"Total B-Count: {total_b_count}")
        if ride_queue == q:
            break
        if b_count == 2:
            b_count = 0
            current_i -= 1

        ride_queue[current_i], ride_queue[current_i - 1] = ride_queue[current_i - 1], ride_queue[current_i]
        current_i -= 1
        b_count += 1
        total_b_count += 1

    if ride_queue == q:
        print(total_b_count)
    else:
        print("Too chaotic")


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    # t = int(input.strip())

    # for t_itr in range(t):
    #     n = int(input().strip())
    #
    #     q = list(map(int, input().rstrip().split()))
    #
    #     minimumBribes(q)

    q = list(map(int, input.rstrip().split()))
    minimumBribes(q)
