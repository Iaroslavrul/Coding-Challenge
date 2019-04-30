import math


def TimeConvert(num):

    # code goes here
    hours = math.floor(num / 60)
    minutes = num - 60*hours
    return str(int(hours))+':'+str(int(minutes))


# keep this function call here
TimeConvert(126)
