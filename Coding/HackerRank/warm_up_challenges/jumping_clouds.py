"""
There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are
thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that
is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads.

Determine the minumum number of jumps it will take to jump from the starting position to the last cloud.
It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

Example
c = [0,1,0,0,0,1,0]

Index the array from 0 .... 6. The number on each cloud is it's index in the list so the player must avoid
the clouds at indices 1 and 5. They could follow these two paths:
0 -> 2 -> 4 -> 6 or 0 -> 2 -> 3 -> 4 -> 6.
The first path takes 3 jumps while the second takes 4. Return 3

Complete the jumpingOnClouds function
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    i = 0
    count = 0
    while i < len(c):
        item = c[i]
       
        if item != 1:
            count += 1
            if count == 2:
                jumps += 1
                count = 0
                print(i, item)
        else:
            count = 0
            jumps += 1
            print(i, item)
        i += 1

    return jumps

if __name__ == '__main__':
    # Driver program
    clouds = [0, 0, 1, 0, 0, 1, 0]
    clouds2 = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    
    print(jumpingOnClouds(clouds2))
    
    
