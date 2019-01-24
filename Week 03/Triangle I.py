''' Triangle I '''
def main():
    ''' Pythagorus's Theorem '''
    num1 = float(input())
    tilted = num1
    base = num1
    num2 = float(input())
    tilted = num2 if num2 > num1 else num1
    base = num2 if num2 < num1 else num1
    num3 = float(input())
    tilted = num3 if num3 > num2 and num3 > num1 else num1 if num1 > num2 else num2
    base = num3 if num3 < num2 and num3 < num1 else num1 if num1 < num2 else num2
    hight = num1 + num2 + num3 - (tilted + base)
    print(calcu(base, hight, tilted))

def calcu(numa, numb, numc):
    ''' for calculate '''
    result = numa**2 + numb**2
    result_much = result if result > numc else numc
    if result == numc**2 or result_much - numc**2 <= 0.01:
        return 'Yes'
    return 'No'

main()
