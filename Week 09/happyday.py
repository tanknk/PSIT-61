"""Happy day"""
def main():
    """try"""
    num = input().split(',')
    count = 0
    for i in range(0, len(num)):
        if int(num[i]) >= 80:
            count += 1
        elif i > 0:
            if int(num[i])-int(num[i-1]) >= 10 and int(num[i]) >= 20:
                count += 1

    print(count)

main()
