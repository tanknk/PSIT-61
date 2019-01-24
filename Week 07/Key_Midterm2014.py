""" key """
def main():
    """ plus 13 """
    num = input()
    num1 = 0
    num2 = (int(num[10:13])*10)
    for i in range(len(num)):
        num1 += int(num[i])
    key = num1+num2
    key += 1000*(key < 1000)
    key = str(key)
    print(key[-4:])

main()
