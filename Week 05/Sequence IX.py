"""Sequence IX"""
def main():
    """Sequence IX"""
    num = int(input())
    for i in range(num):
        print(' '*((num)*3-3*(i+1)), end='')
        for j in range(i+1):
            print('%02d'%(j+1), end=' ')
        for k in range(i, 0, -1):
            print('%02d'%(k), end=' ')
        print()

main()
