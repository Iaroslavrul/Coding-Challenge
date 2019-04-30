def abbrevName(name):
    # code away!
    nameArr = name.split()
    abbreviate = ''
    j = 0
    for i in nameArr:
        word = list(i)
        abbreviate += word[0].upper()
        if j == 0:
            abbreviate += '.'
            j += 1


abbrevName("Sam Harris")
