"""CaesarV1"""
def main():
    """Find True Text"""
    num = int(input())
    text = input()
    line = ""
    for i in text:
        check = ord(i)
        if 65 <= check <= 90:
            check = check+(num%26)
            if check > 90:
                check -= 26
            elif check < 65:
                check += 26
        elif 97 <= check <= 122:
            check = check+(num%26)
            if check > 122:
                check -= 26
            elif check < 97:
                check += 26
        line += chr(check)
    print(line)
main()
