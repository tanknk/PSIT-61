"""Pick"""
import json
def main():
    """check"""
    dic = json.loads(input())
    check = input()
    if check in dic:
        print('Yes')
        print(dic[check])
    else:
        print('No')
main()
