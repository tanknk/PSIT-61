"""Inflation"""
def main():
    """inflation"""
    num = int(float(input())*100)
    loop = int(input())
    for _ in range(loop):
        num = int(num)
        num *= 10381
        num //= 10000
    print('%d.%02d'%((num//100), num%100))

main()
