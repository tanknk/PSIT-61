"""CoPrimeV1"""
def main():
    """GCDvvvvvv1"""
    num1 = int(input())
    num2 = int(input())
    while num2 > 0:
        num1, num2 = num2, (num1%num2)
    if num1 != 1:
        print('NO')
        print(num1)
    else:
        print('YES')
        print(1)

main()
