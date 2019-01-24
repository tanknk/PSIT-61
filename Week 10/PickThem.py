"""PickThem"""
def main():
    """test"""
    num = input().strip('[]').split(', ')
    num1 = []
    for i in range(len(num)):
        if int(num[i])%2 == 0 and int(num[i]) != 0:
            num1.append(num[i])
    if len(num1) >= 1:
        print(*num1, sep='\n')
    else:
        print('Nope')
main()
