"""LastStand"""
def main():
    """test"""
    num = input().strip('[]').split(',')
    num1 = []
    for i in range(len(num)):
        num1.append(num[i][-1])
    print(*num1, sep='\n')

main()
