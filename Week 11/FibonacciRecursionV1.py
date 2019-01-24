""" FibonacciRecursionV1 """
def fibo(num):
    """ fibo recursive """
    if num == 0 or num == 1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)

def main():
    """ main function """
    num = int(input())
    print(fibo(num))

main()
