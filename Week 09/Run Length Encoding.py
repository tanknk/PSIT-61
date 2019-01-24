"""Run Length Encoding"""
def main():
    """test"""
    text = input()
    first_text = text[0]
    count = 0
    for i in range(len(text)):
        if text[i] == first_text:
            count += 1
        elif text[i] != first_text:
            count = str(count)
            print(count+str(first_text), end='')
            first_text = text[i]
            count = 1
    print(str(count)+str(first_text))

main()
