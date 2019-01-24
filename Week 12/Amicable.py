""" Amicable """
def amicable(num):
    """test"""
    count = 0
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            count += i + num//i
    if num**0.5 == int(num**0.5):
        count -= int(num**0.5)
    return count+1


def main(num):
    """ print """
    first = [1]*(num + 1)
    count = 0
    for i in range(2, num+1):
        for j in range(2*i, num+1, i):
            first[j] += i
        second = first[i]
        first_second = amicable(second) if second > num else first[second]
        if first_second == i and i != second:
            count += i
    print(count)

main(int(input()))
