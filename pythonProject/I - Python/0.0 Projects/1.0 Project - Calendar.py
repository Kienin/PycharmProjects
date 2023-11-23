import calendar
year = int(input("What year is it? "))
cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatyear(year))
