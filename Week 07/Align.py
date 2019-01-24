''' Align '''
def main():
    ''' choose position print text '''
    scale = int(input())
    position = input()
    name = input()
    if position == 'left':
        print(name.ljust(scale))
    elif position == 'right':
        print(name.rjust(scale))
    elif position == 'center':
        if len(name)%2 != 0:
            scale += 1
        print(name.center(scale))

main()
