''' Blackjack '''
def main():
    ''' card '''
    nub = 0
    nuba = ''
    for _ in range(int(input())):
        num = input()
        nub += 10 if num in 'JQK' else 11 if num == 'A' else int(num)
        nuba += 'A' if num == 'A' else ''
    while nub > 21 and nuba.count('A'):
        nub -= 10
    print(nub)

main()
