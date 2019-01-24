"""Password"""
import hashlib
def main():
    """test"""
    text = input()
    text2 = hashlib.sha512(text.encode('utf-8')).hexdigest()
    print(text2.upper())
main()
