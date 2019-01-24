"""Ball"""
def ball(num):
    """count"""
    count = 0
    while True:
        num = num*0.6
        if num*100 < 1:
            print(count)
            break
        else:
            count += 1

ball(float(input()))
