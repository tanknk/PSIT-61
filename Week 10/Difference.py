"""Difference"""
def main(first, second):
    """try"""
    set_first = []
    set_second = []
    for _ in range(first):
        member_first = int(input())
        set_first.append(member_first)
    set_first = set(set_first)
    for _ in range(second):
        member_second = int(input())
        set_second.append(member_second)
    set_second = set(set_second)
    set_total = set_first - set_second
    set_total = list(set_total)
    set_total = sorted(set_total)
    print(*set_total, end=' ')

main(int(input()), int(input()))
