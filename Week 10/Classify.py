"""Classify"""
def main():
    """Print All Student"""
    lis_all = []
    nub_dek = []
    while True:
        student = input()
        if student == 'END':
            break
        else:
            lis_all.append(student[0:4])
    lis_all.sort()
    lis_set = list(set(lis_all))
    lis_set.sort()
    for i in range(len(lis_set)):
        num = lis_all.count(lis_set[i])
        nub_dek.append(num)
    for i in range(len(lis_set)):
        if i == 0:
            if lis_all[0][0:2] == lis_all[1][0:2]:
                print(lis_all[0][0:2], int(lis_set[i][2:4]), nub_dek[i])
        elif i > 0:
            if lis_set[i-1][0:2] == lis_set[i][0:2]:
                print('--', int(lis_set[i][2:4]), nub_dek[i])
            elif lis_set[i-1][0:2] != lis_set[i][0:2]:
                print(lis_set[i][0:2], int(lis_set[i][2:4]), nub_dek[i])

main()
