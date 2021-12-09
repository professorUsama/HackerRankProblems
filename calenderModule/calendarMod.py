import calendar

# print(calendar.TextCalendar(firstweekday=6).formatyear(2021))

if __name__ == '__main__':
    month, day, year = map(int,input().split())
    print(calendar.day_name[calendar.weekday(year,month,day)])