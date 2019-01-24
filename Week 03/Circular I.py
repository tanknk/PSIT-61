''' Circular I '''
def main():
    ''' for coordinates '''
    point_me_x = float(input())
    point_me_y = float(input())
    rad = float(input())
    point_mos_x = float(input())
    point_mos_y = float(input())
    print('Yes' if ((point_me_x-point_mos_x)**2+(point_me_y-point_mos_y)**2)**0.5 <= rad else 'No')

main()
