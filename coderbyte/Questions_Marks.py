# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.


def QuestionsMarks(str):

    # code goes here
    numbers = list('123456789')
    strArr = list(str)
    count = 0
    diff = 0
    f = 0
    for i in strArr:
        if i in numbers:
            # нужно отрезать левую часть масива включая i и посмотреть какое следующее число и если оно в суме с i будет == 10 то войти в условие. если сложилось 10, то отсекти опять левую часть и начать подсчет сумы заново
            if  f == 0 or int(f) + int(i) != 10:
                diff = 10 - int(i)
                diff = "%s" % diff
            f = i
        if i == '?' and count != 3 and i not in numbers:
            count += 1
        if count == 3 and i == diff:
            return 'true'
    return 'false'


QuestionsMarks("9???1???9???1???9")
