#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    enc_str = ""
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                enc_str += chr(ord('A') + (ord(s[i]) - ord('A') + k) % 26)
            else:
                enc_str += chr(ord('a') + (ord(s[i]) - ord('a') + k) % 26)
        else:
            enc_str += s[i]

    # enc_str = ""
    # for i in s:
    #     if i.isalpha():
    #         if i.islower():
    #             n = ord(i)
    #             v = chr(n + k)
    #             if ord(v) > ord("z"):
    #                 v = chr(n - 26 + k)
    #             enc_str += v
    #         elif i.isupper():
    #             n = ord(i)
    #             v = chr(n + k)
    #             if ord(v) > ord("Z"):
    #                 v = chr(n - 26 + k)
    #             enc_str += v
    #     else:
    #         enc_str += i

    return enc_str


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())

    s = input
    s = "middle-Outz"
    s = "There's-a-starman-waiting-in-the-sky"
    s = "1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M"
    s = "1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M"

    # k = int(input.strip())
    k = 27
    result = caesarCipher(s, k)
    print(result)

    # fptr.write(result + '\n')
    # fptr.close()
