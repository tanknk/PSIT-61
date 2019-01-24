"""WordSequence I"""
def main():
    """test"""
    text = input()
    for i in range(1, len(text)):
        for j in range(i):
            print(text[j], end="")
        print()
    print(text)
main()
