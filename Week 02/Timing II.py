""" Timing II """
def func1(num):
    ''' Function1's Docstring '''
    day = days(num)
    if day >= 10000 or num < 0:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d"%(day, hours(num), minutes(num), seconds(num)))

def days(num):
    ''' days's Docstring '''
    result = num // 86400
    return result

def hours(num):
    ''' hours's Docstring '''
    result = num % 86400 // 3600
    return result

def minutes(num):
    ''' minutes's Docstring '''
    result = num % 86400 % 3600 // 60
    return result

def seconds(num):
    ''' seconds's Docstring '''
    result = num % 86400 % 3600 % 60
    return result

func1(int(input()))
