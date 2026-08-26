# Read the number of words
n = int(input())

# Dictionary to store each word and its frequency
word_frequency = {}

# Read and count the words
for i in range(n):
    word = input().strip()
    # TODO: Update the frequency of the word
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Print each unique word and its frequency
for word, count in word_frequency.items():
    # TODO: Print the word and count
    print(word, count)