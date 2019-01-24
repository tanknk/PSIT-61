"""function"""
def main():
    """function's"""
    num = int(input())
    grade = 0
    for _ in range(num):
        score = float(input())
        if score >= 95:
            grade += 4
        elif score >= 90:
            grade += 3.5
        elif score >= 85:
            grade += 3
        elif score >= 80:
            grade += 2.5
        elif score >= 75:
            grade += 2
        elif score >= 70:
            grade += 1.5
        elif score >= 65:
            grade += 1
        elif score >= 60:
            grade += 0.5
        else:
            grade += 0
    print('%.2f' %(int((grade/num)*100) / 100))

main()
