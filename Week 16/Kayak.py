"""Kayak"""
def main():
    """Test"""
    _ = input()
    lis = [int(i) for i in input().split()]
    lis.sort()
    result = 0
    while len(lis) > 2:
        diff = [abs(j-i) for i, j in zip(lis, lis[1:])]
        result += min(diff)
        mindex = diff.index(min(diff))
        del lis[mindex:mindex+2]
    print(result)
main()
