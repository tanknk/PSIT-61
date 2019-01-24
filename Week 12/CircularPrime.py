"""CircularPrime"""
def is_prime(num):
    """num"""
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return False if num == 1 else True

def is_circular(cycle):
    """test"""
    for i in cycle:
        if not is_prime(i):
            return False
    return True

def main(num):
    """test"""
    numlist = list((range(1, num+1)))
    ans = 0
    while numlist != []:
        now = str(numlist[0])
        cycle = list()
        for i in range(len(now)):
            cycle_mem = int(now[i:len(now)]+now[0:i])
            if cycle_mem not in cycle:
                cycle.append(cycle_mem)
        if is_circular(cycle):
            for i in cycle:
                if i in numlist:
                    numlist.remove(i)
                    ans += i
            numlist.append(int(now))
        numlist.remove(int(now))
    print(ans)

main(int(input()))
