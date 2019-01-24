""" BusStop I """
def busstop(capacity, station_quantity):
    """ count the passengers """
    bus = sorted([input().split() for i in range(station_quantity)], key=lambda x: int(x[0]))
    count = 0
    lis = []
    for i in bus:
        nub = lis.count(int(i[0]))
        count = count + nub
        lis = lis[nub:]
        lis += [int(j) for j in i[1:] if int(j) > int(i[0])][:capacity-len(lis)]
        lis.sort()
    print(count)
busstop(int(input()), int(input()))
