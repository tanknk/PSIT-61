''' Nearer '''
def main():
    ''' dis ice '''
    alice = int(input())
    bob = int(input())
    dis = int(input())
    alice_1 = max(alice, dis) - min(alice, dis)
    bob_1 = max(bob, dis) - min(bob, dis)
    if alice_1 < bob_1:
        print('Alice', alice_1)
    elif alice_1 > bob_1:
        print('Bob', bob_1)
    else:
        print('Sundaes', alice_1)

main()
