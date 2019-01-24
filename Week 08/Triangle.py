"""main"""
def main():
    """main"""
    num = int(input())
    for i in range(num, 0, -1):
        print((' '*(i*2-2))+('%02d'%(i))+' '*(((num-i)*4)-2)+(('%02d'%(i)) if i != num else ''))

main()
