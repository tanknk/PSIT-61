"""BreachTheDoor"""
def main():
    """Try"""
    text = input()+" "
    keep = ""
    count = 0
    for apl in text:
        if apl.upper() != apl.lower():
            keep += apl
            count += 1
        elif apl.upper() == apl.lower():
            if count >= 7:
                print(keep, end=' ')
                keep = ""
                count = 0
            else:
                keep = ""
                count = 0

main()
