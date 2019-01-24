""" Divide 3Or5 """
def main():
    """ Divide """
    num = int(input())
    plus = 0
    for i in range(1, num+1):
        if i%3 == 0 or i%5 == 0:
            plus += i
    print(plus)

main()
