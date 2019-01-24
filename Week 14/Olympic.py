"""Olympic"""
def main():
    """Find Champion"""
    lis = []
    temp = []
    rank = 0
    for i in range(int(input())):
        cha = input().split()
        lis.append([cha[0], [int(cha[j]) for j in range(1, len(cha))]])
    lis = sorted(lis, key=lambda x: x[0])
    for i in range(-1, -4, -1):
        lis = sorted(lis, key=lambda x: x[1][i], reverse=True)
    for i in range(len(lis)):
        if lis[i][1] not in temp:
            rank = i+1
        else:
            rank = rank
        print(rank, lis[i][0], ' '.join(str(j) for j in lis[i][1]), sum(lis[i][1]))
        temp.append(lis[i][1])
main()
