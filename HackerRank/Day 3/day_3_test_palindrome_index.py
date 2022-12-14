#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here

    def is_palindrome(p):
        # palindrome = True
        # front_index = 0
        # back_index = len(p) - 1
        # while front_index <= back_index:
        #     if p[front_index] != p[back_index]:
        #         palindrome = False
        #     front_index += 1
        #     back_index -= 1
        # return palindrome
        return p == p[::-1]

    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            # Remove left index character
            if is_palindrome(s[0:i] + s[i + 1:]):
                return i
            # Remove right index character
            elif is_palindrome(s[0:len(s) - i - 1] + s[len(s) - i - 1 + 1:]):
                return len(s) - i - 1
            else:
                # Return -1 as string cannot be a palindrome
                return -1

    # Is an empty string or a single character string (both technically palindromes)
    return -1



if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())
    q = 3
    # for q_itr in range(q):
    #     s = input
    #
    #     result = palindromeIndex(s)

    result = palindromeIndex("a")  # -1
    print(result)
    result = palindromeIndex("")  # -1
    print(result)
    result = palindromeIndex("acbdbba")  # -1
    print(result)
    result = palindromeIndex("aaab")  # 3
    print(result)
    result = palindromeIndex("acbba")  # 1
    print(result)


    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
