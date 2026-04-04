import calendar

month, day, year = map(int, input().split())

weekDay = calendar.weekday(year, month, day)

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print(days[weekDay])
