# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def LongestWord(sen):

    # code goes here
    alphabet = list('abcdefghijklmnopqrstuvwxyz1234567890')
    words = sen.split()
    lenLongestWord = 0
    longestWord = ''
    for i in words:
        word = list(i)
        for j in word:
            if j.lower() not in alphabet:
                i = i.replace(j, '')
        if len(i) > lenLongestWord:
            longestWord = i
            lenLongestWord = len(longestWord)
    return longestWord


LongestWord("longest word!!")
