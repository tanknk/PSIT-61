""" isPrime_large """
def func():
    ''' for prime '''
    num = int(input())
    if num < 2:
        return "NO"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "NO"
    return "YES"
def main():
    """ input number """
    print(func())

main()
