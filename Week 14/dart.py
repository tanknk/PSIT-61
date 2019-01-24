"""dart"""
import math as m
def main():
    """Find Point"""
    total = 0
    for _ in range(int(input())):
        nub = input().split(' ')
        nub[0], nub[1] = int(nub[0]), int(nub[1])
        cal = m.hypot(nub[0], nub[1])
        total += 5 if cal <= 2 else 4 if 2 < cal <= 4 else 3 if 4 < cal <= 6 else 2 \
        if 6 < cal <= 8 else 1 if 8 < cal <= 10 else 0
    print(total)
main()
