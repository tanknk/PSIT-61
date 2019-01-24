"""WordSequence II"""
def main(text, character):
    """Print"""
    for i in range(max(len(text), len(character))+1):
        print(character[0:i]+text[i:])
main(input(), input())
