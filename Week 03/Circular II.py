''' Circular II '''
def main():
    ''' for coordinates '''
    # input
    p_1_x = float(input())
    p_1_y = float(input())
    rad_1 = float(input())
    p_2_x = float(input())
    p_2_y = float(input())
    rad_2 = float(input())
    # calculate
    print('Yes' if ((p_1_x-p_2_x)**2+(p_1_y-p_2_y)**2)**0.5 < rad_1+rad_2 else 'No')

main()
