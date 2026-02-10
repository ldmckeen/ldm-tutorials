"""
Shareforce Testing environment

Snakes and Ladders:
For clarity, details of the board are as follows:
The ‘Start’ square is numbered 0, and the ‘Finish’ square is numbered 34.
The board contains the following ladders:
• 1 -> 12
• 5 -> 16
• 11 -> 22
• 15 -> 23
• 20 -> 31
The board contains the following snakes:
• 7 -> 4
• 10 -> 2
• 21 -> 13
• 24 -> 6
• 33 -> 19

"""
import sys
import random

SNAKES_AND_LADDERS_DICT = {
        1: 12,
        5: 16,
        11: 22,
        15: 23,
        20: 31,
        7: 4,
        10: 2,
        21: 13,
        24: 6,
        33: 19
    }

def roll_dice():
    return random.randint(1, 6)


def snakes_and_ladders_1_player():
    """Snakes and Ladders 1 Player."""

    player_1_position = 0
    player_1_roll_count = 0

    game_over = False
    print("Game Starting .....")
    while game_over != True:
        player_1_position += roll_dice()
        player_1_roll_count += 1
        if player_1_position in SNAKES_AND_LADDERS_DICT:
            player_1_position = SNAKES_AND_LADDERS_DICT[player_1_position]
        if player_1_position >= 34:
            game_over = True
    print(".... Game Finished")

    # Question 1: Average Roll Count 1 Player
    return player_1_roll_count


def snakes_and_ladders_2_players():
    """Snakes and Ladders 2 Player."""

    player_1_position, player_2_position = 0, 6
    player_1_roll_count, player_2_roll_count = 0, 0
    player_1_win, player_2_win = False, False

    # Player 1 to start
    player_1_in_play = True
    player_2_in_play = False

    game_over = False

    while game_over != True:
        if player_1_in_play:
            player_1_position += roll_dice()
            player_1_roll_count += 1
            if player_1_position in SNAKES_AND_LADDERS_DICT:
                player_1_position = SNAKES_AND_LADDERS_DICT[player_1_position]
            if player_1_position >= 34:
                player_1_win = True
                game_over = True
            player_1_in_play = False
            player_2_in_play = True
        elif player_2_in_play:
            player_2_position += roll_dice()
            player_2_roll_count += 1
            if player_2_position in SNAKES_AND_LADDERS_DICT:
                player_2_position = SNAKES_AND_LADDERS_DICT[player_2_position]
            if player_2_position >= 34:
                player_2_win = True
                game_over = True
            player_2_in_play = False
            player_1_in_play = True

    # Question 2: Return combined roll count
    # return player_1_roll_count + player_2_roll_count

    # Question 3:  Player 1 Probability
    if player_1_win:
        return True
    else:
        return False

    # Todo: Update functions to take more fine grained input and return once
    """

        Default Return

        if player_1_win:
            return player_1_roll_count
        elif player_2_win:
            return player_2_roll_count
        else:
            return None
    """


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])

    game_amount, game_count = 10000, 10000
    game_number = 1
    average_roll_count_total = 0

    # 1 Player Game: Question 1: Average Roll Count 1 Player
    # print("---- One Player Game ----")
    # print("-------------------------")
    # while game_count > 0:
    #     print(f"Game Number: {game_number}")
    #     average_roll_count_total += snakes_and_ladders_1_player()
    #     game_number += 1
    #     game_count -= 1
    # one_player_result = average_roll_count_total / game_amount
    # print(one_player_result)
    # print("=== END ===\n")

    # 2 Player Game: Question 2: Return combined roll count
    # print("===== Two Player Game ====")
    # print("==========================")
    # while game_count > 0:
    #     print(f"Game Number: {game_number}")
    #     average_roll_count_total += snakes_and_ladders_2_players()
    #     game_number += 1
    #     game_count -= 1
    # two_player_result = average_roll_count_total / game_amount
    # print(two_player_result)
    # print("=== END ===\n")

    # 2 Player Game: Question 3:  Player 1 Probability
    # print("===== Player 1 Probability ====")
    # print("==========================")
    # player_1_win_count = 0
    # while game_count > 0:
    #     print(f"Game Number: {game_number}")
    #     game_result = snakes_and_ladders_2_players()
    #     if game_result == True:
    #         player_1_win_count += 1
    #     game_number += 1
    #     game_count -= 1
    # two_player_result = average_roll_count_total / game_amount
    # print(f"Player 1 won {player_1_win_count} times")
    # print(f"Player 1 win probablity {(player_1_win_count / game_amount) * 100} ")
    # print("=== END ===\n")

    # 2 Player Game: Question 4:  Equal Odds
    print("===== Player Equal Odds ====")
    print("==========================")
    player_1_win_count = 0
    player_2_win_count = 0
    while game_count > 0:
        print(f"Game Number: {game_number}")
        game_result = snakes_and_ladders_2_players()
        if game_result == True:
            player_1_win_count += 1
        elif game_result == False:
            player_2_win_count += 1
        game_number += 1
        game_count -= 1
    print(f"Player 1 won {player_1_win_count} times")
    print(f"Player 1 win probablity {(player_1_win_count / game_amount) * 100} ")
    print(f"Player 2 won {player_2_win_count} times")
    print(f"Player 2 win probablity {(player_2_win_count / game_amount) * 100} ")
    print("=== END ===\n")


"""
Question Answers:
=================

Question 1
If you played the game by yourself, what is the average number of rolls required to finish?
c: 11

Question 2
If you played the game by yourself, what is the average number of rolls required to finish?
d: 19 rolls

Question 3
In a two person game, what is the probability that Player 1 wins?
b. 53 %

Question 4
You decide you want the game to have approximately fair odds, and you do this by changing
the square that Player 2 starts on. From the options below, which square for Player 2’s
start position gives the closest to equal odds for both players?
b. Square 6

"""
