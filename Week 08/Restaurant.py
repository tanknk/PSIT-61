"""Restaurant"""
def func():
    ''' print '''
    num = main(float(input()), float(input()), float(input()), float(input()))
    if num <= 0:
        print('Yes', '%.3f'%abs(num) if num != 0 else '')
    else:
        print('No %.3f'%num)
def main(price, cost, percent, buy):
    ''' calculate '''
    percent = 1 - percent/100
    if price == cost:
        price_per = price*percent
        if buy == 0:
            return 0
        else:
            price_buy_per = (price + buy)*percent
            return price_buy_per-price_per
    else:
        price_buy = price + buy
        if price_buy >= cost:
            return price_buy*percent-price
        elif price < cost and buy == 0:
            return 0
        else:
            return price_buy-price
func()
