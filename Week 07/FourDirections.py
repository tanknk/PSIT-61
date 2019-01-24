''' FourDirections '''
def main():
    ''' for... '''
    cha = input()
    # Line 1
    for _ in cha:
        print('  *  ', end=' ')
    print()
    # Line 2
    for i in cha:
        print(' *    '*(i == 'L'), end='')
        print('   *  '*(i == 'R'), end='')
        print(' ***  '*(i == 'U'), end='')
        print('  *   '*(i == 'D'), end='')
    print()
    # Line 3
    for i in cha:
        print('***** '*(i == 'L' or i == 'R'), end='')
        print('* * * '*(i == 'U' or i == 'D'), end='')
    print()
    # Line 4
    for i in cha:
        print(' *    '*(i == 'L'), end='')
        print('   *  '*(i == 'R'), end='')
        print('  *   '*(i == 'U'), end='')
        print(' ***  '*(i == 'D'), end='')
    print()
    # Line 5
    for _ in cha:
        print('  *  ', end=' ')
    print()

main()
