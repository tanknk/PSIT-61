"""test"""
def main():
    """Main"""
    num = int(input())
    day = num // 86400
    hours = (num % 86400) // 3600
    mins = (num % 3600) // 60
    secs = num % 60
    print(day, hours, mins, secs)

main()
