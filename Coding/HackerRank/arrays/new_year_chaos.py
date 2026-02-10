"""
It's New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker
indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in
front of them to swap positions, but they still wear the original sticker. One person can bribe at most
two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of
bribes or, if anyone has bribed more than two people, print 'Too chaotic'

Example
q = [1,2,3,4,5,6,7,8]
if person 5 bribes person 4, the queue will look like this:
1,2,3,5,4,6,7,8. Only 1 bribe is required. Print 1

q = [4,1,2,3]
person 4 had to bribe 3 people to get to the current position. Print 'Too chaotic'

Complete the function minimumBribes in the
"""
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
    # Adjust q to 0-based indexing for easier calculation
    total_bribes = 0
    # print(q)
    line = [p - 1 for p in q]
    # print(line)
    for i, p in enumerate(line):
        # 1. Check if anyone moved forward more than 2 spots
        # (p is the original index, i is the current index)
        
        if p - i > 2:
            print("Too chaotic")
            return
        
        # 2. Count how many people bribed person 'p'
        # A person who bribed 'p' must be in front of 'p' (from original pos - 1 to current pos)
        # We only need to check from p-1 to i
        for j in range(max(0, p - 1), i):
            if line[j] > p:
                total_bribes += 1
                # print(f"{p}, position: {i}")
                # print(f"total_bribes:{total_bribes}")
    
    print(total_bribes)
    

if __name__ == '__main__':

    q = [2, 1, 5, 3, 4]
    # q = [2, 5, 1, 3, 4]
    q = [5, 1, 2, 3, 7, 8, 6, 4]
    q = [1, 2, 5, 3, 7, 8, 6, 4]

    minimumBribes(q)


