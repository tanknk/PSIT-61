"""Kabata"""
def main(num):
    """test"""
    lis = []
    for _ in range(num):
        lis.append(input())
    for i in range(len(lis)):
        if lis[i].replace('bakka', '').replace('ka', '').replace('ta', '').replace('ba', '')\
         == "" and 'baka' not in lis[i]:
            print('yes')
        else:
            print('no')
main(int(input()))
