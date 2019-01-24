"""Refrigerator"""
def main():
    """Find Nearest Food"""
    quantity = int(input())
    food = input().split()
    food = [int(i) for i in food]
    count = 0
    while True:
        if min(food) == 0:
            break
        else:
            for i in range(quantity):
                food[i] -= 1
                food.sort()
            food[0] += 1
            count += 1
    print(count)

main()
