import datetime
def get_day_of_week(day, month, year):
    date_obj = datetime.datetime(year, month, day)
    day_of_week_int = date_obj.weekday()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[day_of_week_int]
day = 31
month = 8
year = 2019
day_of_week = get_day_of_week(day, month, year)
print("Output:", day_of_week)
