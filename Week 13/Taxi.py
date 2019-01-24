"""Taxi"""
def main(miter, result, time, ans):
    """Find Baht Miter"""
    while miter != 'F':
        miter = miter.split()
        if miter[0] == 'K':
            result += int(miter[1])
        else:
            result += int(miter[2])
            time += int(miter[1])*1.5
        miter = input()
    while result != 0:
        ans += baht(result)
        result -= 1
    ans += 1 if ans%2 == 0 else 0.5*(ans%2 != 0)
    time -= 1 if time%2 == 1 else 0.5*(time%1 == 0.5)
    print(max(int(ans + time), 35))
def baht(kilo):
    """Return Baht to Miter"""
    return 8.5 if kilo >= 81 else 7.5 if 61 <= kilo <= 80 else 6.5 if 41 <= kilo <= 60 else 6 if \
        21 <= kilo <= 40 else 5.5 if 13 <= kilo <= 20 else 5 if 2 <= kilo <= 12 else 35

main(input(), 0, 0, 0)
