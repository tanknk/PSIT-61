"""Largest"""
def largest(num1, num2, num3):
    """again"""
    h01 = int(num1+num2+num3)
    h02 = int(num1+num3+num2)
    h03 = int(num2+num1+num3)
    h04 = int(num2+num3+num1)
    h05 = int(num3+num1+num2)
    h06 = int(num3+num2+num1)
    if h01 >= h02 and h01 >= h03 and h01 >= h04 and h01 >= h05 and h01 >= h06:
        print(h01)
    elif h02 >= h01 and h02 >= h03 and h02 >= h04 and h02 >= h05 and h02 >= h06:
        print(h02)
    elif h03 >= h01 and h03 >= h02 and h03 >= h04 and h03 >= h05 and h03 >= h06:
        print(h03)
    elif h04 >= h01 and h04 >= h02 and h04 >= h03 and h04 >= h05 and h04 >= h06:
        print(h04)
    elif h05 >= h01 and h05 >= h02 and h05 >= h03 and h05 >= h04 and h05 >= h06:
        print(h05)
    else:
        print(h06)

largest(input(), input(), input())
