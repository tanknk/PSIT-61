"""Day2011"""
def main(day, month):
    """Find Day"""
    days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    total_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    return days[(day+total_month[month-1])%7]

print(main(int(input()), int(input())))
