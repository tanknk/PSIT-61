""" OddEvenFighting """
def main():
    """ OddEvenFighting """
    num2 = 0
    num1 = 0
    while True:
        num = int(input())
        if num == 0:
            break
        if num % 2 == 0:
            num2 += num
        else:
            num1 += num
    if num2 > num1:
        print('Even %d'%num2)
    elif num2 < num1:
        print('Odd %d'%num1)
    else:
        print('Draw %d'%num1)

main()
