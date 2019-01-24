"""BreakPassword"""
import hashlib
def main():
    """test"""
    text = input()
    for i in range(100000):
        pass1 = (hashlib.sha512(str('%05d'%i).encode('utf-8')).hexdigest()).upper()
        if pass1 == text:
            print('%05d'%i)
            break

main()
