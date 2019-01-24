"""Duplicate I"""
def main():
    """Find Same Student"""
    group1 = int(input())
    group2 = int(input())
    lis_group1 = []
    lis_group2 = []
    lis_total = []
    for i in range(group1):
        num1 = int(input())
        lis_group1.append(num1)
    for i in range(group2):
        num2 = int(input())
        lis_group2.append(num2)
    lis_group1.sort()
    lis_group2.sort()
    for i in range(len(lis_group1)):
        for j in range(len(lis_group2)):
            if lis_group1[i] == lis_group2[j]:
                lis_total.append(lis_group1[i])
    if lis_total == []:
        print('Nope')
    else:
        lis_total.reverse()
        print(*lis_total, sep='\n')

main()
