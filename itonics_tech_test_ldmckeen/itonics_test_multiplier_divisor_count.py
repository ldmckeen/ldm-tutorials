"""
Function to find the count of multiplier and divisors for each element for an input array
integers.
Thresholds:
array[i] modulo array[j] = 0
array[j] modulo array[i] = 0
"""


def countMultipleDivisors1(arr):

    result_arr = [0 for i in range(len(arr))]

    for i_index, i_num in enumerate(arr):
        count = 0
        for j_index, j_num in enumerate(arr):
            if j_index == i_index:
                continue
            elif j_num % i_num == 0 or i_num % j_num == 0:
                count += 1
        result_arr[i_index] = count

    return result_arr


if __name__ == '__main__':
    input = [6, 8, 9, 12, 24]

    result = countMultipleDivisors1(input)
    print(result)
