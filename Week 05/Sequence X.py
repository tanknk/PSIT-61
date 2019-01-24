''' Sequence X '''
def main():
    ''' for loop '''
    num = int(input())
    for i in range(num):
        print(' '*((num)*3-3*(i+1)), end='')
        for j in range(i+1):
            print('%02d'%(j+1), end=' ')
        for k in range(i, 0, -1):
            print('%02d'%(k), end=' ')
        print()
    for i in range(num-1):
        print(' '*(3*(i+1)), end='')
        for j in range(num-1-i):
            print('%02d'%(j+1), end=' ')
        for k in range(num-2-i):
            print('%02d'%(num-2-k-i), end=' ')
        print()

main()
