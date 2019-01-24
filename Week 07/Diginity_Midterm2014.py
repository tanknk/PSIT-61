''' Diginity_Midterm2014 '''
def main():
    ''' send digi '''
    nub = 0
    while True:
        num = input()
        if int(num) == 0:
            break
        else:
            while len(num) != 1:
                for i in range(len(str(num))):
                    nub += int(num[i])
                num = str(nub)
                nub = 0
            print(num)

main()
