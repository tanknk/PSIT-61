"""compoundInterest"""
def main(baht, interest, year):
    """Find Value"""
    nub = 0
    while nub != year:
        plus = (baht*interest)/100
        baht += plus
        nub += 1
    print('%.2f'%baht)
main(int(input()), float(input()), int(input()))
