"""TicTacToe"""
def main(line1, line2, line3):
    """Find Winner"""
    if line1 == 'XXX' or line1 == 'OOO' or line2 == 'XXX' or line2 == 'OOO' \
    or line3 == 'XXX' or line3 == 'OOO':
        print('X WIN' if line1 == 'XXX' or line2 == 'XXX' or line3 == 'XXX' else 'O WIN')
    elif line1[0] == 'X' and line2[0] == 'X' and line3[0] == 'X' or line1[1] == 'X' \
    and line2[1] == 'X' and line3[1] == 'X' or line1[2] == 'X' and line2[2] == 'X' \
    and line3[2] == 'X':
        print('X WIN')
    elif line1[0] == 'O' and line2[0] == 'O' and line3[0] == 'O' or line1[1] == 'O' \
    and line2[1] == 'O' and line3[1] == 'O' or line1[2] == 'O' and line2[2] == 'O' \
    and line3[2] == 'O':
        print('O WIN')
    elif line1[0] == 'X' and line2[1] == 'X' and line3[2] == 'X' \
    or line1[2] == 'X' and line2[1] == 'X' and line3[0] == 'X':
        print('X WIN')
    elif line1[0] == 'O' and line2[1] == 'O' and line3[2] == 'O' \
    or line1[2] == 'O' and line2[1] == 'O' and line3[0] == 'O':
        print('O WIN')
    else:
        print('DRAW')

main(input(), input(), input())
