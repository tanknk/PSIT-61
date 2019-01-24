"""AlmostMean"""
def main():
    """Find Student that got Almost Mean Score"""
    quantity = int(input())
    student = []
    dic = {}
    score = []
    score_total = 0
    for _ in range(quantity):
        student.append(input().split('\t'))
    for i in range(len(student)):
        dic[student[i][0]] = student[i][1]
    for i in dic:
        if float(dic[i]) >= 0:
            score.append(dic[i])
    for i in range(len(score)):
        score_total += float(score[i])
    score_total = score_total/quantity
    score_new = score_total
    for i in range(quantity):
        check = float(student[i][1])
        if score_total > check:
            if score_new > score_total - check:
                score_new = score_total - check
                lis = student[i]
    print(lis[0], lis[1], sep='\t')
main()
