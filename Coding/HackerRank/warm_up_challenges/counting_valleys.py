"""
An avid hiker keeps meticulous records of their hikes. During thr last hike that took exactly steps
steps, for every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and
end at sea level, and each step up or down represents a 1 unit change in altitude. We define the following
terms:
- A mountain is sequence of consecutive steps above sea level, starting with a step up from sea level and
ending with a step down to sea level.
- A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and
ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example
steps = 8
path = [DDUUUUDD]
The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high.
Finally the hiker returns to sea level and ends the hike.

Return the number of valleys traversed
"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    sea_level_count = 0
    valley_count = 0
    sea_level = True
    valley = False
    for i in path:
        if sea_level_count != 0:
            sea_level = False
            
        if sea_level and i == 'D':
            valley = True
        elif sea_level and i == 'U':
            valley = False
        
        if i == 'D':
            sea_level_count -= 1
        elif i == 'U':
            sea_level_count += 1
        
        if sea_level_count == 0:
            if valley:
                valley_count += 1
                valley = False
            sea_level = True
            
            print("We've hit sea level")
            print(f"Valley Count: {valley_count}")
    
    return valley_count



if __name__ == '__main__':
    # Driver program
    steps = 8
    path = "UDDDUDUU"
    print(countingValleys(steps, path))
    
