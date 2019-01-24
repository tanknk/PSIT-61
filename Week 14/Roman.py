""" Roman """
def main():
    ''' input '''
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    cha = str(input())
    result = 0
    while cha:
        if len(cha) == 1 or roman[cha[0]] >= roman[cha[1]]:
            result += roman[cha[0]]
            cha = cha[1:]
        else:
            result += roman[cha[1]] - roman[cha[0]]
            cha = cha[2:]
    print(result)

main()
