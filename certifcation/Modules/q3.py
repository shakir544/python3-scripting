# Question 3
import datetime as dt

my_dates = ["12/24/2017 13:22", "10/11/17 01:49:59", "12/5/17", "11/29/2017"]

d1 = dt.datetime.strptime(my_dates[0], "%m/%d/%Y %H:%M")

print(d1)