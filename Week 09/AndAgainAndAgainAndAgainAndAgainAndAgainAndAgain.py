"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main(result):
    """CHECK CHARACTER"""
    cha1 = ''
    cha = input().split('.')
    for i in range(len(cha)):
        cha1 += cha[i]
    cha1 = cha1.split(' ')
    for i in range(len(cha1)):
        nub = 0
        for j in range(len(cha1[i])):
            if cha1[i][j] in 'aeiouAEIOU':
                nub += 1
        if nub >= 2:
            result.append(cha1[i])
    result.sort()
    if len(result) > 0:
        print(*result, sep='\n')
    else:
        print('Nope')

main([])
