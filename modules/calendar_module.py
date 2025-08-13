import calendar as c

print(c.calendar(2025))
day_name=c.day_name
for i in day_name:
    print(i[0:3])

print(c.isleap(2025))