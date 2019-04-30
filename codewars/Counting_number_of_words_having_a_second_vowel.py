def count_vowels(string):
    # your code here
    vowels = list('aeiou')
    count = 0
    strArr = string.split()
    for i in strArr:
        word = list(i.lower())
        for j in word:
            if j in vowels:
                count += 1
    return count
count_vowels("Once upon a time")