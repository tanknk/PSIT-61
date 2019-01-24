"""function"""
def main():
    """function's doc"""
    num = int(input())
    if num <= 0:
        print('No')
    elif num%400 == 0:
        print('Yes')
    elif num%4 == 0 and num%100 != 0:
        print('Yes')
    else:
        print('No')

main()
