"""func"""
def main():
    """function's"""
    num1 = int(input())
    num2 = int(input())
    if num1 > num2:
        for i in range(num1, num2-1, -1):
            print(i)
    else:
        for i in range(num1, num2+1):
            print(i)

main()
