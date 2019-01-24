''' SurprisingVote '''
def main():
    ''' for '''
    num1 = float(input())
    num2 = float(input())
    num = num1 - (num2*2)
    if num < 0:
        num = 0
    elif num1 == num2:
        num = 0
    print("Surprising " if num2 - num > 2 else "Not surprising")

main()
