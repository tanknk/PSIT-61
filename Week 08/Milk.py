"""Milk"""
def main(cost, cover, bottle, money):
    """test"""
    num_bottles = money//cost
    num_covers = num_bottles
    while num_covers >= cover and cover > 0:
        temp1 = (num_covers//cover)*bottle
        temp2 = num_covers%cover
        num_bottles += temp1
        num_covers = temp1 + temp2
    print(num_bottles)

main(int(input()), int(input()), int(input()), int(input()))
