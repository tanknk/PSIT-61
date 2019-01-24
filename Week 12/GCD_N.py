"""GCD"""
def main():
    """find gcd"""
    num = int(input())
    lis = []
    for _ in range(num):
        lis.append(int(input()))
        if len(lis) == 2:
            result = gcd(lis[0], lis[1])
            lis = []
            lis.append(result)
    print(*lis)

def gcd(one, two):
    """find gcd"""
    return one if two == 0 else gcd(two, one%two)
main()
