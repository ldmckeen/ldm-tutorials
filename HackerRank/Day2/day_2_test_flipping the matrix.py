#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

"""
Resources:
https://medium.com/@mlgerardvla/hackerrank-flipping-the-matrix-javascript-7f945220ca1b
https://shareablecode.com/snippets/java-solution-for-hackerrank-problem-flipping-the-matrix-UUdP-DJcj
https://programs.programmingoneonone.com/2021/07/hackerrank-flipping-the-matrix-problem-solution.html
https://hackerranksolution.in/flippingthematrixalgo/

https://www.hackerrank.com/challenges/flipping-the-matrix/forum
"""


def flippingMatrix(matrix):
    # Write your code here
    """
    matrix
    [112, 42, 83, 119]
    [56, 125, 56, 49]
    [15, 78, 101, 43]
    [62, 98, 114, 108]

    quadrants
    [0, 1, 1, 0]
    [3, 2, 2, 3]
    [3, 2, 2, 3]
    [0, 1, 1, 0]

    [a, b, b, a]
    [c, d, d, c]
    [c, d, d, c]
    [a, b, b, a]
    """
    sub_matrix_max_sum = 0
    #  Print out Matrix
    print("=========== Matrix =============")
    for i in matrix:
        print(i)
    print("================================")

    sub_matrix_len = int(len(matrix) / 2)
    for i in range(sub_matrix_len):
        for j in (range(sub_matrix_len)):
            # Create Quadrant Matrices
            sub_matrix = []
            base_matrix = matrix[i][j]
            bottom_left_matrix = matrix[2 * sub_matrix_len - i - 1][j]
            top_right_matrix = matrix[i][2 * sub_matrix_len - j - 1]
            bottom_right_matrix = matrix[2 * sub_matrix_len - i - 1][2 * sub_matrix_len - j - 1]

            print("===== bottom_left_matrix =====")
            print(bottom_left_matrix)
            print("===== top_right_matrix =====")
            print(top_right_matrix)
            print("===== bottom_right_matrix =====")
            print(bottom_right_matrix)


            # Append to Submatrix
            sub_matrix.append(base_matrix)
            sub_matrix.append(bottom_left_matrix)
            sub_matrix.append(top_right_matrix)
            sub_matrix.append(bottom_right_matrix)

            # Find Max Sum between Quadrant Matrices
            sub_matrix_max_sum += max(
                max(
                    base_matrix,
                    bottom_left_matrix
                ),
                max(
                    top_right_matrix,
                    bottom_right_matrix
                )
            )
            print("===== sub_matrix =====")
            print(sub_matrix)
            print(f"Max Sum: {sub_matrix_max_sum}")

    return sub_matrix_max_sum


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # q = int(input().strip())
    q = 1
    for q_itr in range(q):
        # n = int(input.strip())
        n = 2

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input.rstrip().split())))

        matrix = [[1, 2, 4, 3], [3, 4, 2, 8], [2, 4, 6, 7], [7, 9, 3, 4]]
        matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
        result = flippingMatrix(matrix)
        print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
