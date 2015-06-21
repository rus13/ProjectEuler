__author__ = 'Ruslan'
import datetime

count = 0
for m in range(1, 13):
    for j in range(1901, 2001):
        if datetime.date(j, m, 1).weekday() == 6:
            count += 1
print(count)