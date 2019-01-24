"""GCD_v1"""
def main():
    """main function"""
    num1 = int(input())
    num2 = int(input())
    while num2 != 0:
        num1, num2 = num2, num1%num2
    print(num1)

main()
