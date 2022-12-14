#!/bin/python3

import math
import os
import random
import re
import sys

"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.
Given an array of  distinct integers, transform the array into a zig zag sequence by permuting the array elements. A sequence will be called a zig zag sequence if the first  elements in the sequence are in increasing order and the last  elements are in decreasing order, where . You need to find the lexicographically smallest zig zag sequence of the given array.
Example.

Now if we permute the array as , the result is a zig zag sequence.

Debug the given function findZigZagSequence to return the appropriate zig zag sequence for the given input array.
"""


def findZigZagSequence(a, n):
    a.sort()
    mid = int(n / 2)
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2
    while (st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')

    return


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])

    for cs in range(1):
        # n = int(input)
        a = list(map(int, input.split()))
        n = len(a)
        findZigZagSequence(a, n)
