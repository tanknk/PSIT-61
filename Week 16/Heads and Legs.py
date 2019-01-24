"""Heads and Legs"""
def main(quantity, legs, rabbit, bird):
    """Find Legs"""
    var = 0
    cal = legs//2
    if quantity == 0 and legs == 0:
        print(rabbit, bird)
    elif (legs//4) > quantity:
        print('Impossible')
    elif cal >= quantity and legs % 2 == 0 and quantity > 0:
        var = ((cal-quantity)*2)
        bird = cal-var
        rabbit = cal-quantity
        print(rabbit, bird)
    else:
        print('Impossible')
main(int(input()), int(input()), 0, 0)
