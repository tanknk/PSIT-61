"""OTP"""
def main():
    """Find Valid OTP"""
    while True:
        nub = input()
        lis = []
        if nub == '0':
            break
        else:
            for i in range(len(nub)):
                for j in range(1):
                    num = nub.count(nub[i][j])
                    lis.append(num)
        if max(lis) == min(lis):
            print('Invalid')
        elif len(nub) == 4:
            print('Valid' if lis.count(2) == 2 or max(lis) == 2 or lis.count(3) == 0\
            else 'Invalid')
        elif len(nub) == 6:
            print('Valid' if lis.count(3) == 3 or lis.count(2) >= 4 \
            else 'Invalid')
        elif len(nub) == 8:
            print('Valid' if lis.count(3) >= 6 or lis.count(2) >= 6 \
            else 'Invalid')
main()
