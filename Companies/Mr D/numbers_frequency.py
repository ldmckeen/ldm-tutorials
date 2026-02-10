"""
Q: You are given a list of numbers, where some numbers may be repeated. How would you find the 'mode' of this list.

A:
numbers = [1, 2, 3, 2, 2, 1]

freq_table = {}
# Build the frequency table
for n in numbers:
    if n in freq_table:
        freq_table[n] += 1
    else:
        freq_table[n] = 1

# Find the max
max_freq = -1
max_number = None
for n in freq_table:
    freq = freq_table[n]
    if freq > max_freq:
        max_freq = freq
        max_number = n
print("The number '{}' appears {} times".format(max_number, max_freq))
"""

# import statistics
# from collections import Counter


def most_frequent(data):
    # Get Frequencies
    counts = {}
    for n in data:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    
    # # Determine Max
    # max = 0
    # max_number = None
    # for number in counts:
    #     freq = counts[number]
    #     if freq > max:
    #         max = freq
    #         max_number = number

    max_count = max(counts, key=counts.get)
    return max_count
    
    # frequency = {}
    #
    # for item in data:
    #     frequency[item] = frequency.get(item, 0) + 1
    #
    # max_count = max(frequency.values())
    # modes = [k for k, v in frequency.items() if v == max_count]
    # return modes
    
    # Using Library Collections Counter Method
    # return statistics.mode(data)
    # counts = Counter(data)
    # return max(counts, key=counts.get)


if __name__ == '__main__':
    numbers_list = [1, 2, 3, 2, 2, 1]
    
    print(most_frequent(numbers_list))

"""
Notes, Items that are drawn, i,e have the same max frequencies in the dictionary,
the order takes precedence, the first key (item that appeared first) will be returned
"""
