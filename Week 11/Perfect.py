""" Perfect """
def prime(num):
    """ return True if n is prime else False """
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True if num != 1 else False

def perfect(num):
    """ return perfect number of n """
    return 2**(num-1)*(2**num-1)

def main():
    """ main function """
    num = int(input())
    ans = 0
    start = 1
    while perfect(start) <= num:
        if prime(start) and prime(2**start-1):
            ans += perfect(start)
        start += 1
    print(ans)

main()
