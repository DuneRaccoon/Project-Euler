from datetime import datetime
from datetime import timedelta

start = datetime(1901,1,1)
end = datetime(2000,12,31)
add_days = timedelta(days=1)
sundays_first_of_month = 0

while True:
    start += add_days
    if start.weekday() == 6 and start.day == 1:
        sundays_first_of_month += 1
    if start == end:
        break

print(sundays_first_of_month)
