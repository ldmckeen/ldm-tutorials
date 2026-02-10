"""
You are given an unordered array consisting of consecutive integeres [1,2,3,...,n] without nay duplicates.
You are allowed to swop any two elements. Find the minimum number of swaps required to sort the array in
ascending order.

Example
arr = [7,1,3,2,4,5,6]

it took 5 swaps to sort the array.

Complete the minimumSwaps function

"""
# !/bin/python3

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

def minimumSwaps(arr):
    swaps = 0
    i = 0
    
    while i < len(arr):
        # The correct value for index i is i + 1
        # If the current value is not i + 1, it belongs elsewhere
        if arr[i] != i + 1:
            # Find the index where arr[i] should actually go
            target_idx = arr[i] - 1
            
            # Swap the current element with the element at its target position
            arr[i], arr[target_idx] = arr[target_idx], arr[i]
            
            # Increment swap counter
            swaps += 1
            
            # Do NOT increment i yet; we need to check if the new
            # value at arr[i] is now correct.
        else:
            # Element is in the right place, move to next index
            i += 1
    
    return swaps


if __name__ == '__main__':
    q = [2, 3, 4, 1, 5]
    # q = [2, 5, 1, 3, 4]
    # q = [5, 1, 2, 3, 7, 8, 6, 4]
    # q = [1, 2, 5, 3, 7, 8, 6, 4]
    
    minimumSwaps(q)


