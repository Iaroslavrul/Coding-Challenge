# Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space.


def LetterCapitalize(str):

    # code goes here
    strArr = str.split()
    newStr = ''
    for i in strArr:
        if i != strArr[0] or newStr != '':
            newStr += ' '
        i = i[0].upper()+i[1:]
        newStr += i
    return newStr


print(LetterCapitalize("Argument goes here"))
