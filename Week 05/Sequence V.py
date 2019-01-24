"""Sequence V"""
def main():
    """Sequence V"""
    num = int(input())
    nub = 0
    for j in range(num, 0, -1):
        nub += 1
        print(j, end=' ')
        if nub == 7:
            print()
            nub = 0

main()
