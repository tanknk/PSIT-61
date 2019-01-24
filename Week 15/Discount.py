"""Discount"""
def main():
    """Find Dis"""
    lis = []
    while True:
        nub = input()
        if nub == 'ENTER':
            break
        else:
            lis.append(int(nub))
    lis.sort()
    if len(lis) >= 25:
        nub = len(lis)//5
        print(sum(lis[nub:]))
    else:
        print(sum(lis) if len(lis) < 6 else sum(lis[1:]) if 6 <= len(lis) < 12 else sum(lis[2:]) \
        if 12 <= len(lis) < 20 else sum(lis[4:]))
main()
