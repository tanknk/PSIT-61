''' GasStations '''
def main(distance, oil):
    ''' for '''
    pumplis = [float(input()) for _ in range(int(input()))]
    temp = []
    start = 0
    end = start + oil
    count = 0
    while True:
        if end >= distance:
            print(count)
            break
        else:
            for i in pumplis:
                if start < i <= end:
                    temp.append(i)
            if temp != []:
                count += 1
                start = temp[-1]
            else:
                print("depleted")
                break
            end = start + oil
            temp = []
main(float(input()), float(input()))
