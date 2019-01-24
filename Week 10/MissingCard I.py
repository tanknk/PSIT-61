"""MissingCard I"""
def main():
    """Check Card"""
    nub = []
    check = {'3S', 'QH', '6C', 'JH', '2H', 'JD', '5D', '9D', 'AS', '9H', '6D', '2S', '10H', \
            'JC', 'AH', '8S', 'KS', '3C', 'AD', 'KH', 'AC', '9C', '7C', '5H', 'QS', '5C',\
             'JS', '10D', '10C', '8D', '5S', 'QC', '3D', 'KC', '2D', 'QD', '10S',\
              '3H', '7H', '4H', '8H', '7S', '7D', '4D', '6H', '9S', '8C', '6S', '4C'\
              , '4S', '2C', 'KD'}
    for _ in range(51):
        nub.append(input())
    nub = set(nub)
    print(*(check-nub))

main()
