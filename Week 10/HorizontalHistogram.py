"""HorizontalHistogram"""
def main():
    """test"""
    cha = sorted(list(input()))
    cha2 = []
    cha3 = ''
    for i in cha:
        if ord(i) < 91:
            cha2.append(i)
    cha = cha[len(cha2)::]
    cha.extend(cha2)
    for i in range(len(cha)):
        cha1 = cha[i]
        cha2 = cha.count(cha1)
        if cha[i] not in cha3:
            print(cha[i]+" :", end=' ')
            for j in range(1, cha2+1):
                print('-', end='')
                if j%5 == 0 and j != cha2:
                    print('|', end='')
            print()
            cha3 += cha[i]
main()
