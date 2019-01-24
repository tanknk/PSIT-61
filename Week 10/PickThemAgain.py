"""PickThemAgain"""
def main():
    """3 OR 5"""
    num = input().split()
    lis = []
    for i in range(len(num)):
        if int(num[i])%3 == 0 or int(num[i])%5 == 0:
            lis.append(num[i])
    lis.reverse()
    if len(lis) >= 1:
        print(*lis, sep='\n')
    elif len(lis) <= 0:
        print('Nope')

main()
