''' Binary '''
def main(num):
    ''' for Decimal transform Binary '''
    binary = [] if num != 0 else [0]
    while True:
        if num < 1:
            break
        binary.append(str(num%2))
        num //= 2
    binary.reverse()
    print(*binary, sep='')

main(int(input()))
