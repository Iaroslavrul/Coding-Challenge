# Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols with several letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter.


def SimpleSymbols(str):

    # code goes here
    alphabet = list('abcdefghijklmnopqrstuvwxyz1234567890')
    strArr = list(str)
    i = 0
    while i + 3 <= len(strArr):
        if strArr[i] == '+' or strArr[i] == '=' and strArr[i+1] in alphabet and strArr[i+2] == '+' or strArr[i+2] == '=':
            i += 3
        else:
            return 'false'
    return 'true'


SimpleSymbols("+d+=3=+s+")
