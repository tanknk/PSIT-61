"""BreachTheDoor"""
def main():
    """main func"""
    text = input()
    result = ""
    for i in text:
        if i.isalpha() == True:
            result += i
        else:
            if len(result) > 6:
                print(result, end=" ")
            result = ""
    if len(result) > 6:
        print(result)

main()
