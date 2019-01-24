"""Missing Number"""
def main():
    """TEST"""
    lis = []
    check = []
    result = []
    num1 = ''
    num = int(input())
    while True:
        num1 = int(input())
        if num1 == 0:
            break
        else:
            lis.append(num1)
    lis.sort()
    for i in range(1, num+1):
        check.append(i)
    for i in range(num):
        if check[i] not in lis:
            result.append(check[i])
    print(*result, sep='\n')

main()
