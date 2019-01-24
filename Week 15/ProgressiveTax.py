"""ProgressiveTax"""
def main(num):
    """Find Value"""
    print(0 if num <= 150000 else int(tax(num)) if num <= 1000000 else int(million(num)))


def tax(num):
    """calculate"""
    total = 0
    if 150000 < num <= 300000:
        total += ((num-150000)*5)/100
    elif 300000 < num <= 500000:
        total += ((num-300000)*10)/100
        num -= (num-300000)
        total += ((num-150000)*5)/100
    elif 500000 < num <= 750000:
        total += ((num-500000)*15)/100
        num -= (num-500000)
        total += ((num-300000)*10)/100
        num -= (num-300000)
        total += ((num-150000)*5)/100
    elif 750000 < num <= 1000000:
        total += ((num-750000)*20)/100
        num -= (num-750000)
        total += ((num-500000)*15)/100
        num -= (num-500000)
        total += ((num-300000)*10)/100
        num -= (num-300000)
        total += ((num-150000)*5)/100
    return total

def million(num):
    """1000000"""
    total = 0
    if 1000000 < num <= 2000000:
        total += ((num-1000000)*25)/100
        num -= (num-1000000)
        total += ((num-750000)*20)/100
        num -= (num-750000)
        total += ((num-500000)*15)/100
        num -= (num-500000)
        total += ((num-300000)*10)/100
        num -= (num-300000)
        total += ((num-150000)*5)/100
    elif 2000000 < num <= 4000000:
        total += ((num-2000000)*30)/100
        num -= (num-2000000)
        total += ((num-1000000)*25)/100
        num -= (num-1000000)
        total += ((num-750000)*20)/100
        num -= (num-750000)
        total += ((num-500000)*15)/100
        num -= (num-500000)
        total += ((num-300000)*10)/100
        num -= (num-300000)
        total += ((num-150000)*5)/100
    elif num > 4000000:
        total += ((num-4000000)*35)/100
        num -= (num-4000000)
        total += ((num-2000000)*30)/100
        num -= (num-2000000)
        total += ((num-1000000)*25)/100
        num -= (num-1000000)
        total += ((num-750000)*20)/100
        num -= (num-750000)
        total += ((num-500000)*15)/100
        num -= (num-500000)
        total += ((num-300000)*10)/100
        num -= (num-300000)
        total += ((num-150000)*5)/100
    return total
main(int(input()))
