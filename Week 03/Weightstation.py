''' WeightStation '''
def main():
    ''' calculate weight '''
    num_average = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num1 = num_average * 4 - (num2 + num3 + num4)
    weight_all = num1 + num2 + num3 + num4

    num_average_add = num_average / 2 + num_average
    num_average_del = num_average - num_average / 2

    if weight_all > 15000:
        print('Overweight')
    elif num_average_del <= num1 <= num_average_add and num_average_del <= num2 <= num_average_add\
    and num_average_del <= num3 <= num_average_add and num_average_del <= num4 <= num_average_add:
        print('Pass', '%.2f'%num1)
    else:
        print('Unbalance')

main()
