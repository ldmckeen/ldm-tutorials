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

def word_count(words):
    word_count = {}

    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1

    max_word = max(word_count, key=word_count.get)
    return max_word


if __name__ == '__main__':
    words = ["one", "two", "three", "two", "two", "one"]
    words = ["one", "two", "three", "two", "two", "one", "three", "three", "two", "three", "three"]
    result = word_count(words)
    print(result)
