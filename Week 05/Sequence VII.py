"""Sequence V"""
def main():
    """Sequence V"""
    num = int(input())
    for i in range(1, num*2):
        if i <= num:
            for j in range(1, i+1):
                print(j, end=' ')
            print()
        else:
            for k in range(1, num*2-i+1):
                print(k, end=' ')
            print()

main()
