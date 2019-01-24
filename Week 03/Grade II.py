"""function"""
def main():
    """func"""
    num1 = float(input())
    if num1 < 0:
        print('ERR')
    elif num1 > 100:
        print('ERR')
    elif num1 >= 95:
        print('A')
    elif num1 >= 90:
        print('B+')
    elif num1 >= 85:
        print('B')
    elif num1 >= 80:
        print('C+')
    elif num1 >= 75:
        print('C')
    elif num1 >= 70:
        print('D+')
    elif num1 >= 65:
        print('D')
    elif num1 >= 60:
        print('F+')
    elif num1 >= 0:
        print('F')

main()
