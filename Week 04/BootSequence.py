"""function"""
def main():
    """function's"""
    var = int(input())
    for i in range(1, var+1):
        if i == var:
            print(i)
        else:
            print(i, end="_")

main()
