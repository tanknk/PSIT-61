"""MacaronBoxSML"""
def main(mac, small, med, large):
    """Print"""
    if mac >= 24:
        large += mac//24
        mac = mac%24
    if 13 <= mac < 24:
        large += mac//13
    if 7 <= mac < 13:
        med += mac//7
    if 0 < mac < 7:
        small += 1
    print(small, med, large, sep='\n')
main(int(input()), 0, 0, 0)
