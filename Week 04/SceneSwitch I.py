"""SceneSwitch I"""
def main():
    """sceneswitch"""
    old = 0
    nub = 0
    count = 0
    color = 'w'
    while True:
        new = input()
        if new == 'End':
            break
        else:
            new = float(new)
            nub += 1
            if nub == 3:
                if color == 'w':
                    if new - old <= 6:
                        count += 1
                        color = '0'
                        nub = 1
                    else:
                        color = 'w'
                        nub = 1
                else:
                    color = 'w'
                    nub = 1
            old = new
    print(count)

main()
