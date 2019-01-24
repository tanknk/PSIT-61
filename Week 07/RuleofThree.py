""" RuleofThree """
def main():
    """ weight """
    check_old = 0
    for _ in range(int(input())):
        price = float(input())
        weight = float(input())
        check = weight/price
        if check >= check_old:
            print_price = price
            print_weight = weight
            check_old = check
    print('%.2f'%print_price, '%.2f'%print_weight)

main()
