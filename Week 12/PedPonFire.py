"""PedPonFire"""
import math as m
def main(num):
    """Test"""
    lis = []
    for _ in range(num):
        lis.append(int(input()))
    newlis = sorted(list(set(lis)))
    gas = int(input())
    gascount = lis.count(gas/2)
    if gascount <= 1:
        count = 0
    else:
        count = m.factorial(gascount)//(m.factorial(gascount-2)*m.factorial(2))
    for i in newlis:
        if i >= gas/2:
            break
        count += lis.count(gas-i)*lis.count(i)
    print(count)
main(int(input()))
