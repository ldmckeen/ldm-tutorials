#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    count_sort_arr = []
    max_num = max(arr)

    print(f"Array: {arr}")
    print(f"Max: {max_num}")
    for i in range(100):
        if i <= max_num:
            index_count = 0
            for j in range(len(arr)):
                if i == arr[j]:
                    index_count += 1
            count_sort_arr.append(index_count)

        else:
            count_sort_arr.append(0)

    return count_sort_arr


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())

    arr = list(map(int, input.rstrip().split()))

    result = countingSort(arr)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
