''' Sequence XI '''
def main():
    ''' for loop '''
    num = int(input())
    nub2 = 1 # bug bottom right
    # print number 2n-1 x 2n-1
    for i in range(1, num*2):
        if i <= num:
            # left print delta 01-n
            for j in range(1, i+1):
                print('%02d'%j, end=' ')
                nub = j
            # add behind half
            for _ in range(nub, num):
                print('%02d'%nub, end=' ')
            # add behind 1/4
            for _ in range(nub, num-1):
                print('%02d'%nub, end=' ')
            # right delta 01-n
            for j in range(nub, 1, -1):
                if j < num:
                    print('%02d'%j, end=' ')
            # rightmost print 01
            print(('%02d'%(1)) if num != 1 else '', end='') # bug when input = 1
            print()
        else:
            # left print delta invert (n-1)-01
            for i in range(1, num*2-i+1):
                print('%02d'%i, end=' ')
                nub = i
            # add behind half
            for _ in range(nub, num):
                print('%02d'%nub, end=' ')
            # right delta (n-2)-01
            for _ in range(nub, num-1):
                print('%02d'%nub, end=' ')
            # rightmost print delta invert (n-1)-01
            for j in range(num-nub2, 0, -1):
                print('%02d'%j, end=' ')
            nub2 += 1
            print()

main()
