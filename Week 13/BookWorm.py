"""BookWorm"""
def main(num):
    """Calculate Book in this function"""
    for _ in range(num):
        time = int(input())
        count = 0
        total = 0
        book_list = [int(input()) for _ in range(int(input()))]
        book_list.sort()
        for i in range(len(book_list)):
            if total + book_list[i] < time:
                total += book_list[i]
            elif total + book_list[i] > time:
                break
            count += 1
        print(count)

main(int(input()))
