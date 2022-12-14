#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if 'PM' in s:
        # With DateTime Library
        s = datetime.strptime(s, '%H:%M:%S%p').strftime('%I:%M:%S')
        # s = s.strip('PM')
        # if int(s[0:2]) < 12:
        #     s = s.replace(s[0:2], str(int(s[0:2]) + 12))
    elif 'AM' in s:
        # With DateTime Library
        s = datetime.strptime(s, '%H:%M:%S%p').strftime('%I:%M:%S')

        # s = s.strip('AM')
        # if int(s[0:2]) >= 12:
        #     s = s.replace(s[0:2], str(int(s[0:2]) - 12))
        #     s = "0" + s
    return s


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])

    # fptr = open('time_conversion.txt', 'w')
    s = input

    result = timeConversion(s)

    print(result)
    # fptr.write(result + '\n')
    #
    # fptr.close()
