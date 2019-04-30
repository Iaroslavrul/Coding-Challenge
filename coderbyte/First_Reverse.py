# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def FirstReverse(str):
    strArr = list(str)
    reverseStr = ''
    i = len(strArr) - 1
    while len(reverseStr) != len(strArr):
        reverseStr += strArr[i]
        i -= 1
    return reverseStr


print(FirstReverse("Argument goes here"))
