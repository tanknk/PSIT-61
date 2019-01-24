"""Quardrant"""
def main(pos_x, pos_y):
    """Print"""
    print('Y' if pos_x == 0 and pos_y != 0 else 'X' if pos_y == 0 and pos_x != 0 \
    else 'O' if pos_x == 0 and pos_y == 0 else 'Q1' if pos_x > 0 and pos_y > 0 else 'Q2' \
    if pos_x < 0 and pos_y > 0 else 'Q3' if pos_x < 0 and pos_y < 0 else 'Q4')
main(int(input()), int(input()))
