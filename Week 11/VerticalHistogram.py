"""VerticalHistogram"""
def main(text):
    """print vertical histogram"""
    his = {}
    for i in text:
        if i not in his:
            his[i] = 0
        his[i] += 1
    for i in range(max(his.values()), 0, -1):
        print("%03d"%i, end="")
        for j in "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper():
            if j in his:
                if his[j] >= i:
                    print(" *", end="")
                else:
                    print("  ", end="")
        print()
    print("   ", end="")
    for i in "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper():
        if i in his:
            print(" "+i, end="")

main(input())
