''' FOR!F-Ball '''
def main():
    ''' check ball '''
    cha = input()
    result = [1, 0, 0]
    for i in range(len(cha)):
        if cha[i] == 'A':
            cha0 = result[0]
            result[0] = result[1]
            result[1] = cha0
        elif cha[i] == 'B':
            cha1 = result[1]
            result[1] = result[2]
            result[2] = cha1
        elif cha[i] == 'C':
            cha0 = result[0]
            result[0] = result[2]
            result[2] = cha0
    for i in range(3):
        if result[i] == 1:
            num = i+1
    print(num)

main()
