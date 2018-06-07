# Question 4
import datetime as dt

my_dates = ["2017-12-28T05:38:09","2017-11-28T05:38:09","2017-10-28T05:38:09" ]

ordered_dates = []

for i in my_dates:
    ordered_dates.append(dt.datetime.strptime(i,"%Y-%m-%dT%H:%M:%S"))

print(ordered_dates.sort())