"""
1
23
456
78910
"""


def solution():

    number = 1  # Starting number
    i = 1  # Starting while loop counter
    newline_counter = 2  # Inner loop counter
    while i <= 4:
        for j in range(1, newline_counter):
            print(number, end='')
            number += 1
        print("")
        newline_counter += 1
        i += 1


if __name__ == '__main__':

    solution()
