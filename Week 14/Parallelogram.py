"""Parallelogram"""
def main(text):
    """test"""
    for i in range(1, len(text)+1):
        print(' '*(len(text)-i)+text[:i])
    for i in range(1, len(text)):
        print(text[i:len(text)])
main(input())
