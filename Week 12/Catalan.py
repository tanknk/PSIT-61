"""Catalan"""
def catalan(num):
    """Find Value"""
    if num == 1:
        return 1
    else:
        return (4*(num-1)+2)/(num+1)*catalan(num-1)
print(int(catalan(int(input()))))
