"""OneTwo"""
def main(num):
    """Sn"""
    lis = ['1', '2']
    for i in range(2, num):
        lis.append(lis[i-1]+lis[i-2])
    print(lis[num-1])
main(int(input()))
