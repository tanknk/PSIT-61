"""LineSorting"""
def main():
    """Sort the Longest Line"""
    num = int(input())
    lis = []
    count = []
    total = []
    for i in range(num):
        num1 = input()
        lis.append(num1)
    for i in range(len(lis)):
        num2 = len(lis[i])
        count.append(num2)
    count.sort()
    for i in range(len(lis)):
        for j in range(len(lis)):
            if count[i] == len(lis[j]):
                total.append(lis[j])
    print(*total, sep='\n')

main()
