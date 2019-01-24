"""Run Length Decoding"""
def main():
    """Test"""
    text = input()
    count = ""
    for i in range(len(text)):
        if text[i].isdigit() == True:
            count += text[i]
        elif text[i].isdigit() == False:
            print(int(count)*text[i], end='')
            count = ""

main()
