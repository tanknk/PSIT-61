"""Safe"""
def safe(password, lock):
    """Find Shortest Way"""
    nub = 0
    for i in range(len(password)):
        if password[i] != lock[i]:
            nub += min(abs(ord(password[i]) - ord(lock[i])), \
                abs(26-abs(ord(password[i]) - ord(lock[i]))))
    return nub
print(safe(input(), input()))
