"""Sequence I"""
def main():
    """Sequence I"""
    num = int(input())
    nub = 1
    nub2 = 1
    count = 3
    while nub2 <= num:
        print(nub, end=' ')
        nub += count
        count += 2
        nub2 += 1

main()
