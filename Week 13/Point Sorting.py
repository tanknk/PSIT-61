"""PointSorting"""
def main(num):
    """Sort Point"""
    for _ in range(num):
        shud = int(input())
        point = []
        for _ in range(shud):
            point.append(list(map(int, input().split())))
        point = sorted(point, key=lambda x: x[1], reverse=True)
        point = sorted(point, key=sum)
        for i, j in point:
            print(i, j)
            point = []
main(int(input()))
