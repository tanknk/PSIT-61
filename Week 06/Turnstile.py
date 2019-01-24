""" Turnstile """
def main():
    """ Turn """
    status = 'Locked'
    roundd = 0
    while True:
        num = input()
        if num == 'END':
            break
        elif status == 'Unlocked':
            if num == 'P':
                roundd += 1
                status = 'Locked'
        elif status == 'Locked':
            if num == 'C':
                status = 'Unlocked'
    print(roundd)

main()
