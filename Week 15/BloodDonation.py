"""BloodDonation"""
def main(num):
    """Find"""
    lis = []
    if num == 17 or 60 <= num <= 70:
        lis.append(num)
        lis.append(int(input()))
        lis.append(int(input()))
        lis.append(input())
    elif 18 <= num <= 59:
        lis.append(num)
        lis.append(int(input()))
        lis.append(int(input()))
    if len(lis) == 3 and lis[1] >= 45:
        if lis[2] == 0:
            print('Yes' if lis[0] < 55 else 'No')
        else:
            print('Yes')
    elif len(lis) == 4 and lis[1] >= 45 and lis[3] == 'True':
        if lis[2] == 0:
            print('Yes' if lis[0] < 55 else 'No')
        else:
            print('Yes')
    else:
        print('No')
main(int(input()))
