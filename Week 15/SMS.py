"""SMS"""
def main():
    """Translate SMS message"""
    data = [(int(input()), int(input())) for _ in range(int(input()))]
    word = ''
    buttons = {1:'-', 2:'ABC', 3:'DEF', \
               4:'GHI', 5:'JKL', 6:'MNO', \
               7:'PQRS', 8:'TUV', 9:'WXYZ'}
    for key, times in data:
        if key == 1:
            wordsize = max(len(word)-times, 0)
            word = word[:wordsize]
        else:
            letters = buttons[key]
            length = len(letters)
            letter = letters[(times-1)%length]
            word = word + letter
    if word == '':
        word = 'null'
    return word

print(main())
