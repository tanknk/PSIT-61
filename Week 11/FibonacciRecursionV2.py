"""FibonacciRecursionV2"""
def fibo(num, fibodic):
    """ fibonacci """
    cache = fibodic
    third = num//2
    first = third+1
    second = third + (num%2 == 1)
    fourth = third - (num%2 == 0)
    if num not in cache:
        if fourth not in cache:
            cache[fourth] = fibo(fourth, cache)
        if third not in cache:
            cache[third] = fibo(third, cache)
        if first not in cache:
            cache[first] = fibo(first, cache)
        cache[num] = cache[first]*cache[second]+cache[third]*cache[fourth]
    return cache[num]

def main(num):
    """ print fibo """
    fibodic = {0:0, 1:1, 2:1}
    print(fibo(num, fibodic))

main(int(input()))
