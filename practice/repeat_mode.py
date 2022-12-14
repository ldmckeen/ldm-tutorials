"""
Q: You are given a list of numbers, where some numbers may be repeated. How would you find the 'mode' of this list.

A: Same as above, but with numbers.

"""

def mode_count(numbers):
    number_count = {}

    for n in numbers:
        if n in number_count:
            number_count[n] += 1
        else:
            number_count[n] = 1

    max_number = max(number_count, key=number_count.get)
    return max_number


if __name__ == '__main__':
    numbers = [1, 2, 3, 2, 2, 1, 4, 4, 4, 4, 4, 4]
    # numbers = [1, 2, 3, 2, 2, 1, 3, 3, 2, 3, 3]
    result = mode_count(numbers)
    print(result)
