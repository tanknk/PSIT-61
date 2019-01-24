"""Seeker"""
def main():
    """Find number and plus all number"""
    num = input()
    lis = []
    count = ''
    for i in num:
        if i.isdigit():
            count += i
        elif count != '':
            lis.append(int(count))
            count = ''
    if count.isdigit():
        lis.append(int(count))
    print(sum(lis))

main()
