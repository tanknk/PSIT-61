"""Diamond I"""
def main(tung, non):
    """Test"""
    lis, result, nub = [], [], 0
    for _ in range(tung):
        lis += [[int(i) for i in input().split()]]
    for i in range(non):
        for j in range(tung):
            nub += lis[j][i]
        result.append(nub)
        nub = 0
    print(max(result))
main(int(input()), int(input()))
