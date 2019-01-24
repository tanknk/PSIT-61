"""NumDays"""
def main(day_start, month_start, day_end, month_end):
    """Find Difference Between Two Days"""
    dic_sum_month = {0:0, 1:31, 2:59, 3:90, 4:120, 5:151, 6:181, 7:212, 8:243, 9:273, \
    10:304, 11:334, 12:365}
    dic_day_month = {0:0, 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day_start_result = dic_sum_month[month_start-1]+day_start
    day_end_result = dic_sum_month[month_end-1]+day_end
    if day_start > dic_day_month[month_start] or day_end > dic_day_month[month_end]:
        print("Impossible")
    else:
        print(abs(day_start_result-day_end_result))
main(int(input()), int(input()), int(input()), int(input()))
