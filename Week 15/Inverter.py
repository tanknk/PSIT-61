"""Inverter"""
def main(text):
    """test"""
    total = ''
    for i in text:
        total += '1' if i == '0' else '0'
    print(int(total) if int(total) != 0 else ' ')
main(input())
