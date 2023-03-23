"""
Healthforce Test
"""


def StringChallenge(num):
    # code goes here
    hours = num // 60
    minutes = num % 60
    hours_minutes = str(hours) + ":" + str(minutes)
    challenge_token = "l902rcwa5"
    token_filler_str = challenge_token[len(hours_minutes):]
    interspersed_result = "".join(i + j for i, j in zip(hours_minutes, challenge_token)) + token_filler_str

    return interspersed_result

def ArrayChallenge(arr):
    """
     # input = [44, 30, 24, 32, 35, 30, 40, 38, 14]
    # input = [10, 12, 4, 5, 9]
    # input = [14, 20, 4, 12, 5, 11]
    """
    max_profit = 0
    for i, i_value in enumerate(arr):
        for j, j_value in enumerate(arr[i+1:]):
            if j_value > i_value:
                profit = j_value - i_value
            if profit > max_profit:
                max_profit = profit

    max_profit = str(max_profit)
    challenge_token = "l902rcwa5"
    token_filler_str = challenge_token[len(max_profit):]
    interspersed_result = "".join(
        i + j for i, j in zip(max_profit, challenge_token)) + token_filler_str

    return interspersed_result


def StringChallenge(strParam):
    """
    String Challenge
    Have the function StringChallenge(str) read str which will be a string of
    roman numerals in decreasing order.
    The numerals being used are:
    I for 1,
    V for 5,
    X for 10,
    L for 50,
    C for 100,
    D for 500 and
    M for 1000.

    Your program should return the same number given by str using a smaller set of roman
    numerals.

    For example: if str is "LLLXXXVVVV" this is 200, so your program should return CC
    because this is the shortest way to write 200 using the roman numeral system given above.
    If a string is given in its shortest form, just return that same string.

    Input: "XXXVVIIIIIIIIII"
    Output: L
    Final Output: Ll902rcwa5

    Input: "DDLL"
    Output: MC
    Final Output: MlC902rcwa5
    """
    roman_num_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman_number_map = [
        [1000, "M"],
        [500, "D"],
        [100, "C"],
        [50, "L"],
        [10, "X"],
        [5, "V"],
        [1, "I"],
    ]
    min_roman = ""
    int_number = 0
    for s in strParam:
        int_number += roman_num_dict[s]

    for i in roman_number_map:
        int_modulo_result = int_number % i[0]
        int_whole_divisor_result = int_number // i[0]
        if int_whole_divisor_result > 0:
            for n in enumerate(int_whole_divisor_result):
                min_roman = min_roman + i[1]
        if int_number % i[0] == 0:
            return i[1]
    # while int_number != 0:


    for key, value in roman_num_dict.items():
        if int_number == value:
            return key
    return roman_num_dict

def printRoman(number):

    roman_number_map = [
        [1, "I"],
        [5, "V"],
        [10, "X"],
        [50, "L"],
        [100, "C"],
        [500, "D"],
        [1000, "M"],
    ]

    min_roman = ""
    map_len_index = len(roman_number_map) - 1
    int_number = number

    while int_number:
        int_whole_divisor_result = int_number // roman_number_map[map_len_index][0]
        int_number %= roman_number_map[map_len_index][0]

        while int_whole_divisor_result:
            # print(roman_number_map[map_len_index][1], end="")
            min_roman = min_roman + roman_number_map[map_len_index][1]
            int_whole_divisor_result -= 1
        map_len_index -= 1

    return min_roman
if __name__ == '__main__':
    # input = [44, 30, 24, 32, 35, 30, 40, 38, 14]
    # input = [10, 12, 4, 5, 9]
    # input = [14, 20, 4, 12, 5, 11]
    # input = "XXXVVIIIIIIIIII"
    # input = "DDLL"
    # result = StringChallenge(input)
    # print(result)

    number = 1100
    # print("Roman value is:", end=" ")
    result = printRoman(number)
    print(result)
    # result = ArrayChallenge(input)
    # print(result)

    # result = StringChallenge(input)
    # print(result)
