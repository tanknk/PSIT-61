''' Donut '''
def main():
    ''' donut '''
    price = int(input())
    buy = int(input())
    free = int(input())
    want = int(input())
    donuts = 0
    price_buy = 0
    buy_free = buy + free
    want_free = want // buy_free
    left = want % buy_free
    if left >= buy:
        want_free += 1
    else:
        donuts += left
        price_buy += (left * price)
    donuts += (buy_free * want_free)
    price_buy += (want_free * buy * price)
    print(price_buy, donuts)

main()
