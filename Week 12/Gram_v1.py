"""Gram_v1"""
def main():
    """print ans"""
    num = input()
    lis = []
    var = 0
    for i in range(len(num)):
        lis.append(num[i:i+2])
    for i in range(len(lis)):
        if lis.count(lis[i]) > var:
            var = lis.count(lis[i])
            ans = lis[i]
    print(ans, var, sep='\n')
main()
