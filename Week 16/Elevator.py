"""Elevator"""
def main(floor, people):
    """Find Floor"""
    lis = []
    while True:
        nub = input()
        if nub == 'END':
            break
        else:
            lis.append(nub)
    for i in lis:
        if people == floor:
            people += 0 if i == 'UP' else -1 if i == 'DOWN' and people > 1 else 0
        elif people == 1:
            people += 1 if i == 'UP' else 0
        elif people < floor:
            people += 1 if i == 'UP' else -1
    print(people)
main(int(input()), int(input()))
