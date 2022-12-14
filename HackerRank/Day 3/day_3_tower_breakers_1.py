#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def towerBreakers_troubleshooting(n, m):
    # Write your code here
    players = [1, 2]
    tower_levels = [*range(1, m+1)]
    towers = [tower_levels] * n
    game_ended = False
    while not game_ended:
        print("\n~<~<~<~<~<~<~=== Start of Turn ===~>~>~>~>~>~>~")

        current_player = players[0]
        print(f"Current Player: {current_player}")
        print("------------------")
        print("Towers in Play")
        print("~~~~~~~~~~~~~~")
        print("||||||||||||||||||")
        for t in towers:
            print(t)
        print("||||||||||||||||||\n")

        chosen_tower_index = 0
        for t in towers:
            if len(t) > len(towers[chosen_tower_index]):
                chosen_tower_index = towers.index(t)

        print(f"Chosen tower: {chosen_tower_index+1}")
        tower_height = len(towers[chosen_tower_index])


        print(f"Tower Height: {tower_height}")
        options = []
        for k in towers[chosen_tower_index]:
            if k == towers[chosen_tower_index][-1]:
                continue
            elif towers[chosen_tower_index][-1] % k == 0:
                options.append(k)
        print(f"Options: {options}")

        if len(options) > 0:
            choice = random.choice(options)
            print(f"Choice: {choice}")
            chosen_tower_copy = towers[chosen_tower_index].copy()
            for c in range(tower_height - choice):
                chosen_tower_copy.pop()
            towers[chosen_tower_index] = chosen_tower_copy
        else:
            game_ended = True
            print("Tough Luck, out of options, you lose")

        # Swop Players
        tmp_pos = players[0]
        players[0] = players[1]
        players[1] = tmp_pos
        print("~o~o~o~o~o~o~=== End of Turn ===~o~o~o~o~o~o~")
        print("_____________________________________________\n")
        if game_ended:
            winner = players[0]
            return winner

def towerBreakers(n, m):
    if m == 1:
        return 2
    else:
        if n % 2 == 1:
            return 1
        else:
            return 2


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())
    # t = int(input.strip())
    t = 2
    # for t_itr in range(t):
    #     first_multiple_input = input.rstrip().split(",")
    #
    #     n = int(first_multiple_input[0])
    #
    #     m = int(first_multiple_input[1])
    #
    #     result = towerBreakers(n, m)

    print("==============================================================================")
    print("New Game")
    print("==============================================================================")
    result = towerBreakers(1, 7)
    print(result)
    print()
    print("==============================================================================")
    print("New Game")
    print("==============================================================================")
    result = towerBreakers(2, 7)
    print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
