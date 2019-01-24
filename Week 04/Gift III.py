"""Gift III"""
def main():
    """loop"""
    num = int(input())
    new = int(input())
    much = new
    sec = 0
    for _ in range(num-1):
        new = int(input())
        if new > much:
            sec = much
            much = new
        elif new < much:
            if new > sec:
                sec = new
    if sec == 0:
        print('Exit')
    else:
        print(sec)

main()
