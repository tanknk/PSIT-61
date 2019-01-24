"""PraSomSib"""
def main(text, check):
    """check"""
    for i in range(len(text)-1):
        count = 0
        count += int(text[i])
        if count < 10:
            next_text = text[i+1::]
            for j in range(len(next_text)):
                count += int(next_text[j])
                if count == 10:
                    check += 1
                    break
                elif count > 10:
                    break
                else:
                    continue
    print(check)
main(input(), 0)
