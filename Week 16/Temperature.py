"""Temperature"""
def main(temp, temp_start, temp_end):
    """Find Temp"""
    result = 0
    temp_cel = 0
    if temp_start == 'C':
        result += (temp*(9/5)+32) if temp_end == 'F' else (temp+273.15) if temp_end == 'K' \
        else (temp+273.15)*(9/5) if temp_end == 'R' else temp
    elif temp_start == 'F':
        temp_cel += (temp-32)/1.8000
        result += (temp_cel*(9/5)+32) if temp_end == 'F' else (temp_cel+273.15) if temp_end == 'K' \
        else (temp_cel+273.15)*(9/5) if temp_end == 'R' else temp_cel
    elif temp_start == 'K':
        temp_cel += (temp-273.15)
        result += (temp_cel*(9/5)+32) if temp_end == 'F' else (temp_cel+273.15) if temp_end == 'K' \
        else (temp_cel+273.15)*(9/5) if temp_end == 'R' else temp_cel
    elif temp_start == 'R':
        temp_cel += (temp-491.67)*(5/9)
        result += (temp_cel*(9/5)+32) if temp_end == 'F' else (temp_cel+273.15) if temp_end == 'K'\
         else (temp_cel+273.15)*(9/5) if temp_end == 'R' else temp_cel
    print('%.2f'%result)

main(float(input()), input(), input())
