"""Median"""
def main():
    """find Med"""
    num = int(input())
    lis = []
    for _ in range(num):
        num1 = input()
        lis.append(int(num1))
    lis.sort()
    if num%2 != 0:
        med = int((num+1)/2)
        print('%.1f'%(lis[med-1]))
    else:
        med = int((num+1)/2)
        print('%.1f'%((lis[med-1]+lis[med])/2))

main()
