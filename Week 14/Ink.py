"""Ink"""
def area(pos_x, pos_y):
    """Return area of circle that pos_x, pos_y is the point on the circumference."""
    return 3.1416*(pos_x**2 + pos_y**2)

def main():
    """Get inputs and print flood time in round up integer."""
    area_rate, num = [int(x) for x in input().split()]
    for _ in range(num):
        pos_x, pos_y = [int(x) for x in input().split()]
        time = area(pos_x, pos_y)/area_rate
        if time != int(time):
            print(int(time+1))
        else:
            print(int(time))

main()
