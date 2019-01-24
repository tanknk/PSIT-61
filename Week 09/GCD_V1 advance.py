''' GCD_v1 '''
def main(num_1, num_2, check_1, check_2):
    ''' for '''
    if num_1 != 0 and num_2 != 0:
        for i in range(1, max(num_1, num_2)):
            if num_1 % i == 0:
                check_1.append(i)
            if num_2 % i == 0:
                check_2.append(i)
        check_max = check_1 if check_1[-1] >= check_2[-1] else check_2
        check_min = check_1 if check_1[-1] < check_2[-1] else check_2
        # print(check_1)
        # print(check_2)
        for i in range(-1, -len(check_max)-1, -1):
            if check_max[i] in check_min:
                result = check_max[i]
                break
        print(result)
    else:
        print(max(num_1, num_2))

main(int(input()), int(input()), [], [])
