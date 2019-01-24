"""CoinChangev1"""
def main(money):
    """Find Money"""
    coin = 0
    coin += money//25
    money = money%25
    coin += money//10
    money = money%10
    coin += money//5
    money = money%5
    coin += money
    print(coin)

main(int(input()))
