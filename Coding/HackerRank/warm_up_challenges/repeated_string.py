"""
There is a string, s, of lowercase English letters that is repeated infinitely many times.
Given an integer n, find and print the number of letter a's in the first n letters of the infinite string.

Example
s = 'abcac'
n = 10

The substring we consider is abcacabcac, the first 10 characters of the infinite string. There are 4
occurrences of 'a' in the substring

Complete the repeatedString function

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    a_count = 0
    s_len = len(s)
    quotent_str = n // s_len
    remainder_str = n % s_len
    print(f"quotent_str:{quotent_str}")
    print(f"remainder_str: {remainder_str}")
    
    for i in s:
        if i == 'a':
            a_count += 1
    
    a_count = a_count * quotent_str
    
    for i in s[:remainder_str]:
        if i == 'a':
            a_count += 1
    
    
    return a_count

if __name__ == '__main__':
    # Driver program
    s = 'aba'
    print(repeatedString(s, 10))
    

