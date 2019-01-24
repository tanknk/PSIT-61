""" Indicator """
def main():
    """ Indicator """
    num1 = int(input())
    num2 = int(input())
    for i in range(num2//2+1):
        print((' '*i)+('*'*num1))
    for i in range(num2//2-1, -1, -1):
        print((' '*i)+('*'*num1))

main()
