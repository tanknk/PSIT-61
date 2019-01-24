"""LetterFrequency"""
def main(text):
    """Check most characters"""
    dic = {}
    for i in text:
        if i in dic:
            dic[i] += 1
        elif i != ' ':
            dic[i] = 1
    max_cha = max(dic.values())
    for j in dic:
        if max_cha == dic[j]:
            print(j)

main(input().lower().rstrip('.'))
