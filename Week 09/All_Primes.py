''' All_Primes '''
def func(num):
    ''' for prime '''
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def main():
    """ input number """
    nub = 0
    num = int(input())
    for i in range(2, num+1):
        num1 = func(i) * i
        if num1 != 0:
            nub += 1
    print(nub)

main()
