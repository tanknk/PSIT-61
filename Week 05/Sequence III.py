"""Sequence III"""
def main():
    """Sequence III"""
    num = int(input())
    for i in range(num):
        for j in range(i+2, num+i+2):
            print(j, end=" ")
        print()

main()
