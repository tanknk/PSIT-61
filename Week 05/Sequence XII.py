''' Sequence XII '''
def main():
    ''' for loop '''
    num = int(input())
    for i in range(1, num+1):
        for j in range(num-i, num):
            print('%02d'%(j+1), end=' ')
        for j in range(num-1, i-1, -1):
            print('%02d'%(j), end=' ')
        for j in range(i+1, num+1):
            print('%02d'%(j), end=' ')
        for j in range(num-1, num-i, -1):
            print('%02d'%(j), end=' ')
        print()
    for i in range(num-1, 0, -1):
        for j in range(num-i, num):
            print('%02d'%(j+1), end=' ')
        for j in range(num-1, i-1, -1):
            print('%02d'%(j), end=' ')
        for j in range(i+1, num+1):
            print('%02d'%(j), end=' ')
        for j in range(num-1, num-i, -1):
            print('%02d'%(j), end=' ')
        print()

main()
