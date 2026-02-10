"""
Q: You are given a list of words. There may be duplicate words in this list.
How would you find the most frequently occurring word in the list.

A:
words = ["one", "two", "three", "two", "two", "one"]
freq_table = {}
# Build the frequency table
for word in words:
    if word in freq_table:
        freq_table[word] += 1
    else:
        freq_table[word] = 1

# Find the max
max_freq = -1
max_word = None
for word in freq_table:
    freq = freq_table[word]
    if freq > max_freq:
        max_freq = freq
        max_word = word
print("The word '{}' appears {} times".format(max_word, max_freq))
"""

from collections import Counter

def most_frequent(data):
    # Get Frequencies
    # counts = {}
    # for word in list:
    #     if word in counts:
    #         counts[word] += 1
    #     else:
    #         counts[word] = 1
    # # return max(counts, key=counts.get)
    
    # Determine Max
    # max = 0
    # max_word = None
    # for word in counts:
    #     freq = counts[word]
    #     if freq > max:
    #         max = freq
    #         max_word = word
    #
    # return max_word

    # Using Library Collections Counter Method
    counts = Counter(data)
    return max(counts, key=counts.get)
    

if __name__ == '__main__':
    words = ["one", "two", "three", "two", "two", "one"]
    
    print(most_frequent(words))
    

"""
Notes, Items that are drawn, i,e have the same max frequencies in the dictionary,
the order takes precedence, the first key (item that appeared first) will be returned
"""
