"""Flatten"""
import json
def main():
    """print lis reverse"""
    num = json.loads(input())
    lis = []
    lis2 = []
    while num != []:
        lis2 = []
        for i in num:
            if isinstance(i, int):
                lis.append(i)
            else:
                lis2.extend(i)
        num = lis2
    lis.sort()
    lis.reverse()
    print(lis)

main()
