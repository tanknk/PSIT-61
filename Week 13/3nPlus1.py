"""3nPlus1"""
def main():
    """test"""
    lis = []
    lis2 = []
    nub = []
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            lis.append(num)
    for i in range(len(lis)):
        while True:
            if lis[i] == 1:
                break
            if lis[i] % 2 == 0:
                lis[i] /= 2
                lis2.append(lis[i])
            elif lis[i] % 2 != 0:
                lis[i] *= 3
                lis[i] += 1
                lis2.append(lis[i])
        nub.append(len(lis2)+1)
        lis2 = []
    print(*nub, sep='\n')
main()
