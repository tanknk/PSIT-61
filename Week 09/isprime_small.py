""" isprime_small """
def func():
    ''' for prime '''
    num = int(input())
    if num < 2:
        return "No"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "No"
    return "Yes"
def main():
    """ input number """
    print(func())

main()
