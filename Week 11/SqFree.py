"""SqFree"""
def sqfree(num):
    """ return 1 if n is sq free else 0 """
    for i in range(2, int(num**0.5)+1):
        if num%(i**2) == 0:
            return 0
    return 1

def main():
    """test"""
    num = int(input())
    count = 0
    for i in range(1, num+1):
        count += sqfree(i)
    print(count)

main()
