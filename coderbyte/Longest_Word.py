# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def LongestWord(sen):

    # code goes here
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    words = sen.split()
    lenLongestWord = 0
    longestWord = ''
    for i in words:
        word = list(i)
        for j in word:
            if j.lower() not in alphabet:
                del word[j]
        if len(i) > lenLongestWord:
            longestWord = i
            lenLongestWord = len(longestWord)
    return longestWord


# keep this function call here
print(LongestWord("Argument goes here"))
