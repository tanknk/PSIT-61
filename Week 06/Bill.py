""" Bill """
def main():
    """ Vat """
    num1 = int(input())
    num2 = (num1*10)/100
    if num2 < 50:
        num2 = 50
        num3 = num1+num2
        num4 = (num3*7)/100
        num5 = num1+num2+num4
        print('%.2f'%num5)
    elif num2 >= 1000:
        num2 = 1000
        num3 = num1+num2
        num4 = (num3*7)/100
        num5 = num1+num2+num4
        print('%.2f'%num5)
    else:
        num3 = num1+num2
        num4 = (num3*7)/100
        num5 = num1+num2+num4
        print('%.2f'%num5)

main()
