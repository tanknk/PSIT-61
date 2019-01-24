"""function"""
def main():
    """function doc"""
    numx = float(input())
    if numx >= 450:
        return when_passed()
    else:
        return when_failed()
def when_passed():
    """docstring"""
    print("Pass")
    print("Process is terminated")
def when_failed():
    """doc"""
    print("Fail")
    print("Process is terminated")

main()
