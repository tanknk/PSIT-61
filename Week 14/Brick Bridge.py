''' Brick Bridge '''
def main(one, five, want):
    ''' for '''
    temp = 0
    nub = 0
    while temp != want:
        if temp <= want and five > 0 and temp + 5 <= want:
            temp += 5
            five -= 1
        elif temp < want and one > 0:
            temp += 1
            one -= 1
            nub += 1
        elif temp < want and temp + one < want:
            nub = -1
            break
    return nub
print(main(int(input()), int(input()), int(input())))
