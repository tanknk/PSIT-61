"""Foodgrade II"""
def main(weight):
    """find"""
    nub = 0
    result = 0
    num = input().split(' ')
    num = [int(i) for i in num]
    num.sort()
    for i in num:
        if i+nub <= weight:
            nub += i
            result += 1
        else:
            break
    print(result)
main(int(input()))
