"""CaesarV2"""
def check(num, text):
    """Check True Sentence in this function"""
    result = ""
    for i in text:
        if i.isalpha():
            ordi = 65 if i.isupper() else 97
            i = chr((ord(i) - ordi + num) % 26 + ordi)
        result += i
    return result

def main(text):
    """Print True Sentence in this function"""
    for i in range(26):
        answer = check(i, text)
        if ('The ' in answer) + (' is ' in answer) + (' a ' in answer):
            print(answer)
            break

main(input())
