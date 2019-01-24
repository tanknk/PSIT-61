"""ValidVar"""
def main():
    """Print"""
    reverse = ['if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'break', 'return'\
    , 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def', 'None']
    for _ in range(int(input())):
        nub = input()
        if nub in reverse or nub[0] in '1234567890':
            print('Invalid')
        elif '<' in nub or '.' in nub or '@' in nub or '%' in nub or '!' in nub or '#' in nub or \
        '$' in nub or '>' in nub or '^' in nub or '&' in nub or '~' in nub or ',' in nub\
        or '?' in nub or ';' in nub or ':' in nub or '/' in nub or '|' in nub or '(' in nub\
        or ')' in nub or "'" in nub or '฿' in nub or '=' in nub or '-' in nub or '+' in nub or \
        '[' in nub or ']' in nub or '{' in nub or '}' in nub or '*' in nub or '\"' in nub or\
        '\\' in nub or ' ' in nub:
            print('Invalid')
        else:
            print('Valid')
main()
