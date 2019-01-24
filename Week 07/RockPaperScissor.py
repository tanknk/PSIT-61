''' RockPaperScissor '''
def main():
    ''' count score winner A and B '''
    cha = input()
    score = [0, 0, 0]
    check1 = ['SP', 'PR', 'RS']
    check2 = ['PS', 'RP', 'SR']
    for i in range(0, len(cha), 2):
        check = cha[i]+cha[i+1]
        if check in check1:
            score[0] += 1
        elif check in check2:
            score[1] += 1
    if score[0] > score[1]:
        print('A win', str(score[0])+'-'+str(score[1]))
    elif score[1] > score[0]:
        print('B win', str(score[1])+'-'+str(score[0]))
    else:
        print('DRAW', score[1])

main()
