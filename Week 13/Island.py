"""Island"""
def main(num, lis, count):
    """Print"""
    for _ in range(num[0]):
        lis.append(list(map(int, input().split())))
    for i in range(num[0]):
        for j in range(num[1]):
            if lis[i][j]:
                lis = check(i, j, lis, num[1], num[0])
                count += 1
    print(count)

def check(numy, numx, lis, col, row):
    """Calculate"""
    lis[numy][numx] = 0
    for i in range(-(numy != 0), 1 + (numy != row - 1)):
        for j in range(-(numx != 0), 1 + (numx != col - 1)):
            if lis[numy+i][numx+j]:
                lis = check(numy+i, numx+j, lis, col, row)
    return lis
main(list(map(int, input().split())), [], 0)
