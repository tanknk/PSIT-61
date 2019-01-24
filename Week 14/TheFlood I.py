"""The Flood I"""
def main():
    """Find Sandbag"""
    sandbag = [int(i) for i in input().split()]
    count = 0
    while 0 not in sandbag:
        sandbag.sort()
        for i in range(len(sandbag)):
            sandbag[i] -= 1
        sandbag[0] += 1
        count += 1
    print(count)

main()
