"""Ascending"""
def main():
    """try"""
    num = int(input())
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = [num, num1, num2, num3, num4]
    num5.sort()
    for i in range(5):
        print(num5[i])

main()
